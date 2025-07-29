from sqlalchemy.orm import Session
from . import models, schemas

def create_kpaform(db: Session, form: schemas.KPAFormCreate):
    db_kpaform = models.KPAForm(**form.dict())
    db.add(db_kpaform)
    db.commit()
    db.refresh(db_kpaform)
    return db_kpaform
