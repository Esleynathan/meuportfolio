# API Documentation - Portfolio Backend

**Base URL**: `http://localhost:8000/api`
**Django Admin**: `http://localhost:8000/admin`
**Interactive Docs (Swagger)**: `http://localhost:8000/api/docs/`
**OpenAPI Schema**: `http://localhost:8000/api/schema/`

---

## Endpoints Overview

The API follows REST principles and provides full CRUD operations where appropriate.

### Projects API

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/projects/` | Lista todos os projetos | No |
| POST | `/api/projects/` | Cria novo projeto | Yes (Admin) |
| GET | `/api/projects/{id}/` | Detalhes de um projeto | No |
| PUT | `/api/projects/{id}/` | Atualiza projeto completo | Yes (Admin) |
| PATCH | `/api/projects/{id}/` | Atualiza projeto parcialmente | Yes (Admin) |
| DELETE | `/api/projects/{id}/` | Remove projeto | Yes (Admin) |
| GET | `/api/projects/featured/` | Lista apenas projetos em destaque | No |

#### Query Parameters

- `?search=django` - Busca em título, descrição e tecnologias
- `?ordering=order` - Ordena por campo order (crescente)
- `?ordering=-created_at` - Ordena por data de criação (decrescente)
- `?ordering=-updated_at` - Ordena por data de atualização

#### Project Object Schema

```json
{
  "id": 1,
  "title": "Sistema de Blog",
  "slug": "sistema-de-blog",
  "description": "Blog completo com Django e PostgreSQL",
  "detailed_description": "Sistema completo de blog com autenticação...",
  "technologies": "Django, PostgreSQL, Docker",
  "github_url": "https://github.com/user/projeto",
  "live_url": "https://projeto.com",
  "image": "http://localhost:8000/media/projects/blog.png",
  "featured": true,
  "order": 1,
  "created_at": "2025-12-04T10:30:00Z",
  "updated_at": "2025-12-04T10:30:00Z"
}
```

---

### Skills API

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/skills/` | Lista todas as skills | No |
| POST | `/api/skills/` | Cria nova skill | Yes (Admin) |
| GET | `/api/skills/{id}/` | Detalhes de uma skill | No |
| PUT | `/api/skills/{id}/` | Atualiza skill completa | Yes (Admin) |
| PATCH | `/api/skills/{id}/` | Atualiza skill parcialmente | Yes (Admin) |
| DELETE | `/api/skills/{id}/` | Remove skill | Yes (Admin) |
| GET | `/api/skills/by-category/` | Filtra skills por categoria | No |

#### Query Parameters

- `?search=python` - Busca por nome da skill
- `?category=Frontend` - Filtra por categoria
- `?ordering=order` - Ordena por campo order (crescente)
- `?ordering=-proficiency_level` - Ordena por nível de proficiência

#### Categories

- `Frontend` - Tecnologias de frontend (Angular, React, Vue, etc.)
- `Backend` - Tecnologias de backend (Django, Flask, Node.js, etc.)
- `Database` - Bancos de dados (PostgreSQL, MySQL, MongoDB, etc.)
- `DevOps` - Ferramentas DevOps (Docker, Kubernetes, CI/CD, etc.)
- `Tools` - Ferramentas diversas (Git, VSCode, etc.)
- `Others` - Outras habilidades

#### Skill Object Schema

```json
{
  "id": 1,
  "name": "Python",
  "category": "Backend",
  "proficiency_level": 4,
  "description": "Linguagem principal de backend",
  "icon": "python-icon.svg",
  "order": 1,
  "created_at": "2025-12-04T10:30:00Z"
}
```

**Proficiency Levels:**
- `1` = Básico
- `2` = Intermediário
- `3` = Avançado
- `4` = Expert

---

### Contacts API

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/contacts/` | Lista mensagens recebidas | Yes (Admin) |
| POST | `/api/contacts/` | Envia nova mensagem | No |
| GET | `/api/contacts/{id}/` | Detalhes de uma mensagem | Yes (Admin) |

**Importante**: PUT, PATCH e DELETE não são permitidos via API. Gerenciamento de mensagens deve ser feito via Django Admin.

#### Contact Object Schema

```json
{
  "id": 1,
  "name": "João Silva",
  "email": "joao@example.com",
  "subject": "Oportunidade de Trabalho",
  "message": "Olá, gostaria de conversar sobre...",
  "read": false,
  "created_at": "2025-12-04T10:30:00Z"
}
```

---

## Request Examples

### 1. Listar Todos os Projetos

```bash
curl http://localhost:8000/api/projects/
```

**Response (200 OK)**:
```json
[
  {
    "id": 1,
    "title": "Portfolio Full-Stack",
    "slug": "portfolio-full-stack",
    "description": "Sistema completo com Django REST API",
    "technologies": "Django, Angular, Docker",
    "featured": true,
    ...
  }
]
```

---

### 2. Criar Novo Projeto (Admin)

```bash
curl -X POST http://localhost:8000/api/projects/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{
    "title": "Sistema de Blog",
    "description": "Blog com Django e PostgreSQL",
    "detailed_description": "Sistema completo de blog com autenticação, posts, comentários e categorias.",
    "technologies": "Django, PostgreSQL, Docker",
    "github_url": "https://github.com/user/projeto",
    "live_url": "https://projeto.com",
    "featured": true,
    "order": 1
  }'
```

**Response (201 Created)**:
```json
{
  "id": 2,
  "title": "Sistema de Blog",
  "slug": "sistema-de-blog",
  ...
}
```

---

### 3. Buscar Projetos com Django

```bash
curl "http://localhost:8000/api/projects/?search=django"
```

---

### 4. Listar Projetos em Destaque

```bash
curl http://localhost:8000/api/projects/featured/
```

**Response**: Retorna apenas projetos com `featured: true`

---

### 5. Filtrar Skills por Categoria

```bash
curl "http://localhost:8000/api/skills/by-category/?category=Frontend"
```

**Response (200 OK)**:
```json
[
  {
    "id": 3,
    "name": "Angular",
    "category": "Frontend",
    "proficiency_level": 4,
    ...
  },
  {
    "id": 4,
    "name": "TypeScript",
    "category": "Frontend",
    "proficiency_level": 4,
    ...
  }
]
```

---

### 6. Enviar Mensagem de Contato (Público)

```bash
curl -X POST http://localhost:8000/api/contacts/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "João Silva",
    "email": "joao@example.com",
    "subject": "Oportunidade de Trabalho",
    "message": "Olá, gostaria de conversar sobre uma vaga na minha empresa..."
  }'
```

**Response (201 Created)**:
```json
{
  "id": 5,
  "name": "João Silva",
  "email": "joao@example.com",
  "subject": "Oportunidade de Trabalho",
  "message": "Olá, gostaria de conversar sobre...",
  "read": false,
  "created_at": "2025-12-04T14:25:00Z"
}
```

---

### 7. Listar Todas as Skills Ordenadas

```bash
curl "http://localhost:8000/api/skills/?ordering=order"
```

---

## Authentication

### Admin Operations

Para operações de criação, edição e exclusão, é necessário autenticação de administrador.

#### Obter Token (Django REST Framework Token Authentication)

```bash
curl -X POST http://localhost:8000/api-auth/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "your_password"
  }'
```

**Response**:
```json
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

#### Usar Token nas Requisições

```bash
curl -X POST http://localhost:8000/api/projects/ \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
  -H "Content-Type: application/json" \
  -d '{"title": "Novo Projeto", ...}'
```

---

## Error Responses

### 400 Bad Request
Dados inválidos ou campos obrigatórios faltando.

```json
{
  "title": ["Este campo é obrigatório."],
  "email": ["Digite um endereço de email válido."]
}
```

### 401 Unauthorized
Token de autenticação inválido ou ausente.

```json
{
  "detail": "As credenciais de autenticação não foram fornecidas."
}
```

### 403 Forbidden
Sem permissão para realizar a operação.

```json
{
  "detail": "Você não tem permissão para executar essa ação."
}
```

### 404 Not Found
Recurso não encontrado.

```json
{
  "detail": "Não encontrado."
}
```

### 405 Method Not Allowed
Método HTTP não permitido para este endpoint.

```json
{
  "detail": "Método \"DELETE\" não é permitido."
}
```

---

## CORS Configuration

O backend está configurado para aceitar requisições do frontend Angular:

**Allowed Origins:**
- `http://localhost:4200` (Angular dev server)
- `http://127.0.0.1:4200`

**Allowed Methods:**
- GET, POST, PUT, PATCH, DELETE, OPTIONS

**Allowed Headers:**
- Authorization, Content-Type, Accept

---

## Rate Limiting

Atualmente não há rate limiting configurado. Em produção, considere implementar:
- Django REST Framework Throttling
- Nginx rate limiting
- CloudFlare (se aplicável)

---

## Testing the API

### Using Django Admin
1. Acesse: http://localhost:8000/admin
2. Login com superusuário criado
3. Crie projetos e skills de teste
4. Teste os endpoints via Swagger ou curl

### Using Swagger UI
1. Acesse: http://localhost:8000/api/docs/
2. Explore todos os endpoints interativamente
3. Teste requests diretamente pela interface

### Using Postman
1. Importe o OpenAPI schema: http://localhost:8000/api/schema/
2. Configure base URL: `http://localhost:8000`
3. Adicione token de autenticação se necessário

---

## Future Enhancements

- [ ] Paginação para grandes listas
- [ ] Filtros avançados (data range, múltiplas tecnologias)
- [ ] Upload de imagens via API (atualmente apenas via Admin)
- [ ] Versionamento da API (`/api/v1/`, `/api/v2/`)
- [ ] GraphQL endpoint (opcional)
- [ ] WebSocket para notificações em tempo real

---

**Documentação gerada em**: 2025-12-04
**Versão da API**: 1.0 (MVP 1)
