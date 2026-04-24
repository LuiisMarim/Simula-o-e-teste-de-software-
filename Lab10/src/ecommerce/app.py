"""API de e-commerce usada nos testes não funcionais.

A aplicação é propositalmente pequena para permitir execução local, mas expõe
endpoints suficientes para validar desempenho, carga, estresse, escalabilidade e
segurança com pytest, pytest-benchmark, requests/httpx e Locust.
"""

from __future__ import annotations

import html
import time
from collections import defaultdict, deque
from dataclasses import dataclass
from hashlib import sha256
from threading import Lock
from typing import Deque

from fastapi import FastAPI, Header, HTTPException, Request, Response
from pydantic import BaseModel, Field

RATE_LIMIT_PER_MINUTE = 100
WINDOW_SECONDS = 60
ADMIN_TOKEN_HASH = sha256("black-friday-admin-token".encode()).hexdigest()


@dataclass(frozen=True)
class Product:
    id: int
    name: str
    price: float
    stock: int


PRODUCTS: dict[int, Product] = {
    1: Product(id=1, name="Notebook Gamer", price=4899.90, stock=120),
    2: Product(id=2, name="Smartphone", price=2499.90, stock=300),
    3: Product(id=3, name="Headset", price=299.90, stock=900),
}


class CheckoutRequest(BaseModel):
    product_id: int = Field(gt=0)
    quantity: int = Field(default=1, gt=0, le=10)


class SearchResult(BaseModel):
    query: str
    results: list[dict]


class RateLimiter:
    """Rate limiter em memória por IP para validar 100 req/min/IP."""

    def __init__(self, limit: int = RATE_LIMIT_PER_MINUTE, window: int = WINDOW_SECONDS):
        self.limit = limit
        self.window = window
        self._hits: dict[str, Deque[float]] = defaultdict(deque)
        self._lock = Lock()

    def allow(self, key: str, now: float | None = None) -> bool:
        current_time = time.time() if now is None else now
        with self._lock:
            hits = self._hits[key]
            while hits and current_time - hits[0] >= self.window:
                hits.popleft()
            if len(hits) >= self.limit:
                return False
            hits.append(current_time)
            return True

    def reset(self) -> None:
        with self._lock:
            self._hits.clear()


rate_limiter = RateLimiter()
app = FastAPI(title="Black Friday E-commerce Test API", version="1.0.0")


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.headers.get("X-Forwarded-For") or (request.client.host if request.client else "local")
    if not rate_limiter.allow(client_ip):
        return Response(
            content='{"detail":"Rate limit excedido: maximo de 100 req/min/IP"}',
            status_code=429,
            media_type="application/json",
            headers={"Retry-After": "60"},
        )
    return await call_next(request)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "availability_target": "99.9%"}


@app.get("/produto/{product_id}")
def get_product(product_id: int) -> dict:
    product = PRODUCTS.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "stock": product.stock,
    }


@app.post("/compra")
def checkout(payload: CheckoutRequest) -> dict:
    product = PRODUCTS.get(payload.product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    if payload.quantity > product.stock:
        raise HTTPException(status_code=409, detail="Estoque insuficiente")
    return {
        "status": "approved",
        "product_id": product.id,
        "quantity": payload.quantity,
        "total": round(product.price * payload.quantity, 2),
    }


@app.get("/buscar", response_model=SearchResult)
def search(q: str) -> dict:
    blocked_tokens = ["' or '1'='1", "drop table", "--", "<script", "onerror=", "; rm"]
    normalized = q.lower()
    if any(token in normalized for token in blocked_tokens):
        raise HTTPException(status_code=400, detail="Entrada rejeitada por validação de segurança")
    safe_query = html.escape(q, quote=True)
    results = [
        {"id": p.id, "name": p.name, "price": p.price}
        for p in PRODUCTS.values()
        if safe_query.lower() in p.name.lower()
    ]
    return {"query": safe_query, "results": results}


@app.get("/admin")
def admin_area(authorization: str | None = Header(default=None)) -> dict:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token obrigatório")
    token = authorization.removeprefix("Bearer ").strip()
    if sha256(token.encode()).hexdigest() != ADMIN_TOKEN_HASH:
        raise HTTPException(status_code=403, detail="Acesso negado")
    return {"area": "admin", "status": "authorized"}
