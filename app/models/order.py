from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from enum import Enum
from app.database import Base

class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total = Column(Float, nullable=False)
    status = Column(SQLEnum(OrderStatus), default=OrderStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    
    order = relationship("Order", back_populates="items")
    product = relationship("Product")
    
    @property
    def product_name(self):
        return self.product.name if self.product else "Produto removido"