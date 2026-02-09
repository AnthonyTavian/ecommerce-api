# 🛒 E-commerce API

API REST completa para gerenciamento de e-commerce.

## 🚧 Em desenvolvimento

- [x] Setup inicial
- [ ] Autenticação JWT
- [ ] CRUD de Produtos
- [ ] Sistema de Pedidos
- [ ] Testes
- [ ] Deploy

## 🚀 Como executar
```bash
# Clone o repositório
git clone https://github.com/AnthonyTavian/ecommerce-api.git

# Entre na pasta
cd ecommerce-api

# Crie a venv
python -m venv venv
venv\Scripts\activate

# Instale dependências
pip install -r requirements.txt

# Configure o .env
copy .env.example .env

# Execute
uvicorn app.main:app --reload
```

## 📚 Documentação

Acesse: http://localhost:8000/docs

## 🛠️ Tecnologias

- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT
- Docker

## 👤 Autor

Anthony Tavian