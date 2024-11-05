from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


# create a new instance of the Order model with the provided data
def create(db: Session, order):
    db_order = models.Order(
        customer_name=order.customer_name,
        description=order.description
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


# retrieve all rows in table
def read_all(db: Session):
    return db.query(models.Order).all()


# retrieve a specific data by its id.
def read_one(db: Session, order_id):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


# update the database record with the new data
def update(db: Session, order_id, order):
    db_order = db.query(models.Order).filter(models.Order.id == order_id)
    update_data = order.model_dump(exclude_unset=True)
    db_order.update(update_data, synchronize_session=False)
    db.commit()
    return db_order.first()


# query the database for the specific order to delete
def delete(db: Session, order_id):
    db_order = db.query(models.Order).filter(models.Order.id == order_id)
    db_order.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
