from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


# Create a new instance of the Sandwich model with the provided data
def create(db: Session, sandwiches):
    db_sandwiches = models.Sandwich(
        customer_name=sandwiches.customer_name,
        description=sandwiches.description
    )
    db.add(db_sandwiches)
    db.commit()
    db.refresh(db_sandwiches)
    return db_sandwiches


# retrieve all rows in table
def read_all(db: Session):
    return db.query(models.Sandwich).all()


# retrieve a specific data by its id.
def read_one(db: Session, sandwiches_id):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwiches_id).first()


# update the database record with the new data
def update(db: Session, sandwiches_id, sandwiches):
    db_sandwiches = db.query(models.Sandwich).filter(models.Sandwich.id == sandwiches_id)
    update_data = sandwiches.model_dump(exclude_unset=True)
    db_sandwiches.update(update_data, synchronize_session=False)
    db.commit()
    return db_sandwiches.first()


# query the database for the specific sandwich to delete
def delete(db: Session, sandwiches_id):
    db_sandwiches = db.query(models.Sandwich).filter(models.Sandwich.id == sandwiches_id)
    db_sandwiches.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
