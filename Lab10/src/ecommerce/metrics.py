"""Funções auxiliares para cálculo de métricas não funcionais."""

from __future__ import annotations

import statistics


def percentile(values: list[float], p: float) -> float:
    if not values:
        raise ValueError("A lista de valores não pode ser vazia")
    ordered = sorted(values)
    index = (len(ordered) - 1) * (p / 100)
    lower = int(index)
    upper = min(lower + 1, len(ordered) - 1)
    weight = index - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def throughput(total_requests: int, total_seconds: float) -> float:
    if total_seconds <= 0:
        raise ValueError("O tempo total deve ser maior que zero")
    return total_requests / total_seconds


def horizontal_efficiency(real_throughput: float, baseline_throughput: float, nodes: int) -> float:
    if baseline_throughput <= 0 or nodes <= 0:
        raise ValueError("Baseline e quantidade de nós devem ser positivos")
    ideal = baseline_throughput * nodes
    return (real_throughput / ideal) * 100


def availability(success: int, total: int) -> float:
    if total <= 0:
        raise ValueError("Total deve ser maior que zero")
    return (success / total) * 100


def summarize_response_times(values: list[float]) -> dict:
    return {
        "min_ms": min(values),
        "avg_ms": statistics.mean(values),
        "p95_ms": percentile(values, 95),
        "p99_ms": percentile(values, 99),
        "max_ms": max(values),
    }
