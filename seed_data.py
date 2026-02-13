from app.database import SessionLocal
from app.models.user import User
from app.models.category import Category
from app.models.product import Product
from app.utils.security import get_password_hash

def seed_database():
    db = SessionLocal()
    
    try:
        # Verifica se já tem dados
        if db.query(User).first():
            print("⚠️  Banco já tem dados. Pulando seed.")
            return
        
        print("🌱 Populando banco de dados...")
        
        # Criar admin
        admin = User(
            email="admin@ecommerce.com",
            full_name="Administrador",
            hashed_password=get_password_hash("admin123"),
            is_admin=True
        )
        db.add(admin)
        
        # Criar usuário comum
        user = User(
            email="user@example.com",
            full_name="Usuário Teste",
            hashed_password=get_password_hash("user123"),
            is_admin=False
        )
        db.add(user)
        
        db.commit()
        
        # Criar categorias
        categorias = [
            Category(name="Eletrônicos", description="Produtos eletrônicos e tecnologia"),
            Category(name="Roupas", description="Vestuário e acessórios"),
            Category(name="Livros", description="Livros e materiais educativos"),
            Category(name="Casa", description="Produtos para casa e decoração"),
        ]
        
        for cat in categorias:
            db.add(cat)
        
        db.commit()
        
        # Criar produtos
        produtos = [
            Product(name="Notebook Dell", description="i7, 16GB RAM", price=3500.00, stock=10, category_id=1),
            Product(name="iPhone 15", description="128GB", price=7500.00, stock=5, category_id=1),
            Product(name="Mouse Logitech", description="Sem fio", price=150.00, stock=50, category_id=1),
            Product(name="Camiseta Básica", description="100% algodão", price=49.90, stock=100, category_id=2),
            Product(name="Calça Jeans", description="Slim fit", price=159.90, stock=30, category_id=2),
            Product(name="Tênis Nike", description="Corrida", price=399.00, stock=20, category_id=2),
            Product(name="Clean Code", description="Robert C. Martin", price=89.90, stock=15, category_id=3),
            Product(name="Python Fluente", description="Luciano Ramalho", price=95.00, stock=12, category_id=3),
            Product(name="Luminária LED", description="Regulável", price=79.90, stock=25, category_id=4),
            Product(name="Tapete Decorativo", description="2x3m", price=299.00, stock=8, category_id=4),
        ]
        
        for prod in produtos:
            db.add(prod)
        
        db.commit()
        
        print("✅ Banco populado com sucesso!")
        print("👤 Admin: admin@ecommerce.com / admin123")
        print("👤 User: user@example.com / user123")
        print(f"📦 {len(categorias)} categorias criadas")
        print(f"🛍️  {len(produtos)} produtos criados")
        
    except Exception as e:
        print(f"❌ Erro ao popular banco: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()