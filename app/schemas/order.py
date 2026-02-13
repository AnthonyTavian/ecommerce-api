from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from app.models.order import OrderStatus

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0, description="Quantidade deve ser maior que 0")

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float
    product_name: str  
    
    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    items: List[OrderItemCreate] = Field(min_length=1, description="Pedido deve ter pelo menos 1 item")

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total: float
    status: OrderStatus
    created_at: datetime
    updated_at: datetime
    items: List[OrderItemResponse]
    
    class Config:
        from_attributes = True

class OrderStatusUpdate(BaseModel):
    status: OrderStatus