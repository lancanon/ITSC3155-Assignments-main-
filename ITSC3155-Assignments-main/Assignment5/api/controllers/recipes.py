from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import models, schemas


# create a new instance of the Recipe model with the provided data
def create(db: Session, recipe):
    db_recipe = models.Recipe(
        sandwich_id=recipe.sandwich_id,
        resource_id=recipe.resource_id,
        amount=recipe.amount
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


# retrieve all rows in table
def read_all(db: Session):
    return db.query(models.Recipe).all()


# retrieve a specific data by its id.
def read_one(db: Session, recipe_id):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()


# update the database record with the new data
def update(db: Session, recipe_id, recipe):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    update_data = recipe.model_dump(exclude_unset=True)
    db_recipe.update(update_data, synchronize_session=False)
    db.commit()
    return db_recipe.first()


# query the database for the specific recipe to delete
def delete(db: Session, recipe_id):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    db_recipe.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
