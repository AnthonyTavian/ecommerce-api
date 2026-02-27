from app.models.category import Category
from app.models.product import Product

def test_create_order(client, user_token, db):
    category = Category(name="Test Category", description="Test")
    db.add(category)
    db.commit()
    
    product = Product(name="Test Product", price=100.00, stock=10, category_id=category.id)
    db.add(product)
    db.commit()
    
    response = client.post(
        "/orders",
        json={
            "items": [
                {"product_id": product.id, "quantity": 2}
            ]
        },
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["total"] == 200.00
    assert len(data["items"]) == 1
    assert data["items"][0]["product_name"] == "Test Product"  
    assert data["items"][0]["quantity"] == 2
    assert data["items"][0]["price"] == 100.00

def test_create_order_insufficient_stock(client, user_token, db):
    category = Category(name="Test Category", description="Test")
    db.add(category)
    db.commit()
    
    product = Product(name="Test Product", price=100.00, stock=5, category_id=category.id)
    db.add(product)
    db.commit()
    
    response = client.post(
        "/orders",
        json={
            "items": [
                {"product_id": product.id, "quantity": 10}  
            ]
        },
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 400
    assert "insuficiente" in response.json()["detail"]

def test_list_my_orders(client, user_token, db):
    response = client.get(
        "/orders",
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
