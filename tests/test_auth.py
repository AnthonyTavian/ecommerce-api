def test_register_user(client):
    """Testa registro de novo usuário"""
    response = client.post(
        "/auth/register",
        json={
            "email": "newuser@test.com",
            "full_name": "New User",
            "password": "password123"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "newuser@test.com"
    assert data["full_name"] == "New User"
    assert "id" in data

def test_register_duplicate_email(client, test_user):
    """Testa erro ao registrar email duplicado"""
    response = client.post(
        "/auth/register",
        json={
            "email": "test@test.com",  
            "full_name": "Another User",
            "password": "password123"
        }
    )
    assert response.status_code == 400
    assert "já cadastrado" in response.json()["detail"]

def test_login_success(client, test_user):
    """Testa login com credenciais corretas"""
    response = client.post(
        "/auth/login",
        json={"email": "test@test.com", "password": "test123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client, test_user):
    """Testa login com senha incorreta"""
    response = client.post(
        "/auth/login",
        json={"email": "test@test.com", "password": "wrongpassword"}
    )
    assert response.status_code == 401

def test_login_nonexistent_user(client):
    """Testa login de usuário que não existe"""
    response = client.post(
        "/auth/login",
        json={"email": "noexist@test.com", "password": "test123"}
    )
    assert response.status_code == 401

def test_get_current_user(client, user_token):
    """Testa obter dados do usuário logado"""
    response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@test.com"

def test_get_current_user_invalid_token(client):
    """Testa acesso com token inválido"""
    response = client.get(
        "/auth/me",
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401