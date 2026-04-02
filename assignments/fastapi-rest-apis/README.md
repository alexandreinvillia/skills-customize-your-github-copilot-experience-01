# 📘 Assignment: APIs REST com FastAPI

## 🎯 Objective

Construir uma API REST básica usando FastAPI para criar, listar, atualizar e remover recursos, aplicando boas práticas de rotas e validação de dados.

## 📝 Tasks

### 🛠️ Criando Endpoints CRUD

#### Description
Implemente uma API para gerenciar uma lista de tarefas (to-do) com operações de criação, leitura, atualização e remoção.

#### Requirements
Completed program should:

- Criar endpoints `GET /tasks`, `GET /tasks/{task_id}`, `POST /tasks`, `PUT /tasks/{task_id}` e `DELETE /tasks/{task_id}`.
- Retornar códigos HTTP apropriados para sucesso e erro (por exemplo, 200, 201, 404).
- Armazenar os dados em memória usando lista ou dicionário.

### 🛠️ Validação e Respostas da API

#### Description
Use modelos Pydantic para validar os dados de entrada e padronizar as respostas da API.

#### Requirements
Completed program should:

- Definir um modelo `TaskCreate` para entrada e um modelo `Task` para saída.
- Garantir que `title` seja obrigatório e que `completed` tenha valor padrão `False`.
- Retornar mensagens claras de erro quando o recurso não for encontrado.
