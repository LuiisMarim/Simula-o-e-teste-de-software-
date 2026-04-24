"""Cenário de carga realista para Black Friday.

Execução sugerida:
locust -f locustfile.py --users 10000 --spawn-rate 500 --host http://localhost:8000
"""

from locust import HttpUser, between, task


class UsuarioEcommerce(HttpUser):
    wait_time = between(1, 3)

    @task(7)
    def ver_produto(self):
        self.client.get("/produto/1", name="GET /produto/{id}")

    @task(2)
    def buscar_produto(self):
        self.client.get("/buscar", params={"q": "Notebook"}, name="GET /buscar")

    @task(1)
    def finalizar_compra(self):
        self.client.post("/compra", json={"product_id": 1, "quantity": 1}, name="POST /compra")
