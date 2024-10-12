from sqlalchemy.orm import Session
from models.user import UserModel, UserCreate
from models.product import ProductModel, ProductCreate
from models.order import OrderModel, OrderCreate

# Работа с пользователями
def get_users(db: Session):
    return db.query(UserModel).all()

def create_user(db: Session, user: UserCreate):
    db_user = UserModel(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Работа с продуктами
def get_products(db: Session):
    return db.query(ProductModel).all()

def create_product(db: Session, product: ProductCreate):
    db_product = ProductModel(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_orders(db: Session):
    return db.query(OrderModel).all()

def create_order(db: Session, order: OrderCreate):
    db_order = OrderModel(product_name=order.product_name, quantity=order.quantity)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
