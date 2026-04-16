# Suíte de Testes REST com pytest - ReqRes

## API escolhida
- **API:** ReqRes
- **Documentação:** https://reqres.in/

## Justificativa da escolha
A ReqRes foi escolhida porque é uma API pública, simples de consumir com `requests`, possui endpoints de listagem, busca por recurso, criação, atualização, remoção e autenticação, atendendo ao enunciado da atividade.

## Estrutura do projeto
```text
meu-projeto/
|-- test_api.py
|-- requirements.txt
|-- README.md
```

## Instalação
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Execução
```bash
pytest test_api.py -v
```

Para salvar a saída em arquivo:
```bash
pytest test_api.py -v > resultado.txt
```

## Dependências
O arquivo `requirements.txt` contém exatamente as bibliotecas pedidas no enunciado:
- `requests`
- `pytest`
- `jsonschema`

## Testes implementados
A suíte cobre os requisitos mínimos pedidos:

1. **GET em coleção**: valida `200 OK` e lista não vazia em `/users?page=2`
2. **GET em recurso existente com schema**: valida a resposta de `/users/2` com `jsonschema`
3. **GET em recurso inexistente**: valida `404 Not Found` em `/users/23`
4. **POST criando recurso**: valida `201 Created` e presença de `id` em `/users`
5. **PATCH atualizando recurso**: valida `200 OK` e alteração do campo `job`
6. **DELETE**: valida `204 No Content` em `/users/2`
7. **Envio de dados inválidos**: valida erro `4xx` em `/login` sem senha
8. **Autenticação com e sem credencial**:
   - login válido retorna `200` e `token`
   - login sem credenciais retorna `4xx`
9. **Fixture com `@pytest.fixture`**: cria um usuário no setup e envia `DELETE` no teardown
10. **Tempo de resposta**: valida resposta menor que `2,0 s`

## Observações
- O código foi escrito apenas em Python, sem uso de Postman ou Insomnia.
- Nenhum teste usa `time.sleep()`.
- Todas as funções de teste possuem docstring, como exigido.
- A ReqRes pode exigir o header `x-api-key: reqres-free-v1`. O projeto já envia esse header por padrão.
- Também é possível sobrescrever a URL base com variável de ambiente:

```bash
export BASE_URL="https://reqres.in/api"
```
