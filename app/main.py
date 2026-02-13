from fastapi import FastAPI
from app.config import settings
from app.database import engine, Base
from app.models import User, Category, Product
from app.routers import auth, categories, products

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API REST completa para e-commerce com autenticação JWT"
)

app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(products.router)

@app.get("/")
def read_root():
    return {
        "message": "E-commerce API está rodando!",
        "version": settings.APP_VERSION,
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "ok", "database": "connected"}