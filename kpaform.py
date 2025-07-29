from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db
from typing import List

router = APIRouter()

@router.post("/kpaformdata", response_model=schemas.KPAFormOut)
def create_kpaform(form: schemas.KPAFormCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_kpaform(db=db, form=form)
    except Exception as e:
        print("❌ ERROR creating form:", e)  # Debug log
        raise HTTPException(status_code=500, detail=str(e))
