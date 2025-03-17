from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
from models import Message, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/messages/")
def create_message(message: str, db: Session = Depends(get_db)):
    db_message = Message(message=message)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message