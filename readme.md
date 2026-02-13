# 🛒 E-commerce API

![Tests](https://img.shields.io/badge/tests-15%20passed-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-87%25-yellowgreen)
![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688)


API REST completa para gerenciamento de e-commerce com autenticação JWT, sistema de pedidos e controle de estoque.

## 🚀 Tecnologias

- **Backend:** Python 3.11, FastAPI
- **Banco de Dados:** PostgreSQL
- **ORM:** SQLAlchemy
- **Autenticação:** JWT (JSON Web Tokens)
- **Validação:** Pydantic
- **Containerização:** Docker, Docker Compose
- **Testes:** Pytest (em desenvolvimento)

## ✨ Funcionalidades

### 🔐 Autenticação & Autorização
- Registro de usuários
- Login com JWT tokens
- Proteção de rotas por autenticação
- Sistema de permissões (Admin/User)

### 📦 Categorias
- CRUD completo de categorias
- Validação de nome único
- Proteção de deleção (verifica produtos vinculados)

### 🛍️ Produtos
- CRUD completo de produtos
- Relacionamento com categorias
- Controle de estoque
- Filtros avançados:
  - Por categoria
  - Por faixa de preço
  - Busca por nome
  - Paginação

### 🛒 Sistema de Pedidos
- Criação de pedidos com múltiplos itens
- Validação automática de estoque
- Cálculo automático de total
- Histórico de preços (salva preço no momento da compra)
- Atualização de estoque ao criar pedido
- Gerenciamento de status (pending, paid, shipped, delivered, cancelled)
- Usuários veem apenas seus pedidos
- Admins gerenciam todos os pedidos

## 🏗️ Arquitetura
```
ecommerce-api/
├── app/
│   ├── models/          # Modelos do banco de dados (SQLAlchemy)
│   ├── routers/         # Endpoints da API
│   ├── schemas/         # Schemas de validação (Pydantic)
│   ├── utils/           # Utilitários (segurança, dependências)
│   ├── config.py        # Configurações
│   ├── database.py      # Conexão com banco
│   └── main.py          # App principal
├── tests/               # Testes automatizados
├── seed_data.py         # Script para popular banco
├── docker-compose.yml   # Configuração Docker
├── Dockerfile           # Imagem Docker
└── requirements.txt     # Dependências Python
```

## 🔧 Como Executar

### Pré-requisitos
- Python 3.11+
- Docker e Docker Compose
- Git

### Opção 1: Com Docker (Recomendado)
```bash
# Clone o repositório
git clone https://github.com/AnthonyTavian/ecommerce-api.git
cd ecommerce-api

# Copie o .env de exemplo
cp .env.example .env

# Edite o .env com suas configurações
# Importante: Mude o SECRET_KEY!

# Suba os containers
docker-compose up --build

# A API estará disponível em http://localhost:8000
# Documentação interativa: http://localhost:8000/docs
```

### Opção 2: Ambiente Local
```bash
# Clone o repositório
git clone https://github.com/AnthonyTavian/ecommerce-api.git
cd ecommerce-api

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt

# Configure o .env
cp .env.example .env
# Edite com suas configurações

# Certifique-se que o PostgreSQL está rodando
docker-compose up -d db

# Popule o banco de dados (opcional)
python seed_data.py

# Execute a API
uvicorn app.main:app --reload

# Acesse: http://localhost:8000/docs
```

## 📡 Endpoints Principais

### Autenticação
```
POST   /auth/register      - Criar conta
POST   /auth/login         - Login (retorna JWT)
GET    /auth/me            - Dados do usuário logado
```

### Categorias
```
GET    /categories         - Listar categorias (público)
GET    /categories/{id}    - Buscar por ID (público)
POST   /categories         - Criar (admin)
PUT    /categories/{id}    - Atualizar (admin)
DELETE /categories/{id}    - Deletar (admin)
```

### Produtos
```
GET    /products           - Listar com filtros (público)
GET    /products/{id}      - Buscar por ID (público)
POST   /products           - Criar (admin)
PUT    /products/{id}      - Atualizar (admin)
DELETE /products/{id}      - Deletar (admin)
```

### Pedidos
```
POST   /orders                    - Criar pedido (autenticado)
GET    /orders                    - Meus pedidos (autenticado)
GET    /orders/{id}               - Detalhes do pedido (autenticado)
GET    /orders/admin/all          - Todos os pedidos (admin)
PUT    /orders/{id}/status        - Atualizar status (admin)
```

## 🧪 Dados de Teste

Após rodar `python seed_data.py`:

**Admin:**
- Email: `admin@ecommerce.com`
- Senha: `admin123`

**Usuário:**
- Email: `user@example.com`
- Senha: `user123`

**Produtos:** 10 produtos em 4 categorias diferentes

## 🔒 Autenticação

A API usa JWT (JSON Web Tokens) para autenticação.

**Como usar:**

1. Faça login em `/auth/login`
2. Copie o `access_token` retornado
3. No Swagger UI, clique em "Authorize" (cadeado)
4. Cole o token (sem "Bearer")
5. Agora você pode acessar rotas protegidas

## 🐳 Variáveis de Ambiente

Crie um arquivo `.env` baseado no `.env.example`:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ecommerce
SECRET_KEY=sua-chave-super-secreta-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**⚠️ IMPORTANTE:** Mude o `SECRET_KEY` em produção!

## 🚧 Próximas Melhorias

- [ ] Testes automatizados (Pytest)
- [ ] CI/CD com GitHub Actions
- [ ] Upload real de imagens de produtos
- [ ] Sistema de carrinho persistente
- [ ] Notificações por email
- [ ] Webhooks para pagamentos
- [ ] Rate limiting
- [ ] Logs estruturados

## 📚 Documentação

A documentação interativa está disponível em:
- **Swagger UI:** `/docs`
- **ReDoc:** `/redoc`

## 👤 Autor

**Anthony Tavian de Castro Alves**

- GitHub: [@AnthonyTavian](https://github.com/AnthonyTavian)
- LinkedIn: [anthonytavian](https://www.linkedin.com/in/anthonytavian/)

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e de portfólio.

---

⭐ Se este projeto te ajudou, considere dar uma estrela!