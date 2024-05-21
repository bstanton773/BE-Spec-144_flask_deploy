from sqlalchemy.orm import Session
from database import db
from models.product import Product


def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            # Create a new instance of Product
            new_product = Product(name=product_data['name'], price=product_data['price'])
            # Add that instance to the db
            session.add(new_product)
            session.commit()
        session.refresh(new_product)
        return new_product
