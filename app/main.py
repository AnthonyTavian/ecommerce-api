from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API REST completa para e-commerce com autenticação JWT"
)

@app.get("/")
def read_root():
    return {
        "message": "E-commerce API está rodando!",
        "version": settings.APP_VERSION,
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}