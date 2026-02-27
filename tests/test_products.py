from app.models.category import Category
from app.models.product import Product

def test_create_product_as_admin(client, admin_token, db):
    category = Category(name="Test Category", description="Test")
    db.add(category)
    db.commit()
    
    response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "description": "Test Description",
            "price": 99.99,
            "stock": 10,
            "category_id": category.id
        },
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 99.99

def test_create_product_as_user_forbidden(client, user_token, db):
    category = Category(name="Test Category", description="Test")
    db.add(category)
    db.commit()
    
    response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "price": 99.99,
            "stock": 10,
            "category_id": category.id
        },
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 403

def test_list_products_public(client, db):
    category = Category(name="Test Category", description="Test")
    db.add(category)
    db.commit()
    
    product = Product(
        name="Test Product",
        price=99.99,
        stock=10,
        category_id=category.id
    )
    db.add(product)
    db.commit()
    
    response = client.get("/products")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["name"] == "Test Product"

def test_filter_products_by_price(client, db):
    category = Category(name="Test Category", description="Test")
    db.add(category)
    db.commit()
    
    product1 = Product(name="Cheap", price=10.00, stock=10, category_id=category.id)
    product2 = Product(name="Expensive", price=1000.00, stock=10, category_id=category.id)
    db.add_all([product1, product2])
    db.commit()
    

    response = client.get("/products?max_price=100")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Cheap"

def test_search_products_by_name(client, db):
    category = Category(name="Test Category", description="Test")
    db.add(category)
    db.commit()
    
    product = Product(name="Notebook Dell", price=3500.00, stock=10, category_id=category.id)
    db.add(product)
    db.commit()
    
    response = client.get("/products?search=notebook")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert "Notebook" in data[0]["name"]
