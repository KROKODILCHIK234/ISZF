from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.user import UserCreate, UserRead
from models.product import ProductCreate, ProductRead
from models.order import OrderCreate, OrderRead
from services.db_service import get_users, create_user, get_products, create_product, get_orders, create_order
from database import get_db

api_router = APIRouter()

# Маршруты для пользователей
@api_router.get("/users/", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)

@api_router.post("/users/", response_model=UserRead)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

# Маршруты для продуктов
@api_router.get("/products/", response_model=list[ProductRead])
def list_products(db: Session = Depends(get_db)):
    return get_products(db)

@api_router.post("/products/", response_model=ProductRead)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)


@api_router.get("/orders/", response_model=list[OrderRead])
def list_orders(db: Session = Depends(get_db)):
    return get_orders(db)

@api_router.post("/orders/", response_model=OrderRead)
def add_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)
