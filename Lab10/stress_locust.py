"""Cenário de estresse/spike para achar ponto de quebra.

Execução:
locust -f stress_locust.py --users 15000 --spawn-rate 1000 --headless --host http://localhost:8000 --csv resultado_estresse
"""

from locust import HttpUser, constant_pacing, task


class UsuarioEstresse(HttpUser):
    wait_time = constant_pacing(0.1)

    @task
    def endpoint_critico(self):
        with self.client.get("/produto/1", catch_response=True, name="GET /produto/{id}") as response:
            if response.elapsed.total_seconds() > 0.5:
                response.failure("Tempo de resposta acima de 500ms")
            elif response.status_code in {429, 503}:
                response.failure("Sistema limitando ou indisponível sob estresse")
