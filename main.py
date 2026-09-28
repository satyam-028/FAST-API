from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


# Create all database tables
models.Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI()

# app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "CRUD API is running successfully"
    }

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ==========================================
# CREATE
# ==========================================

@app.post("/items/", response_model=schemas.Item)
def create_item(
    item: schemas.ItemCreate,
    db: Session = Depends(get_db)
):
    
    db_item = models.Item(**item.model_dump())

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


# ==========================================
# READ ALL
# ==========================================

@app.get("/items/", response_model=list[schemas.Item])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    print("hello API")
    items = (
        db.query(models.Item)
        .offset(skip)
        .limit(limit)
        .all()
    )
    print("Hello read Items 1 run before return")
    return items


# ==========================================
# READ ONE
# ==========================================

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    print("Hello api")
    
    item = (
        db.query(models.Item)
        .filter(models.Item.id == item_id)
        .first()
    )
    print("Hello read Items 12 run")
    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return item


# ==========================================
# UPDATE
# ==========================================

@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(
    item_id: int,
    item: schemas.ItemCreate,
    db: Session = Depends(get_db)
):
    db_item = (
        db.query(models.Item)
        .filter(models.Item.id == item_id)
        .first()
    )
    print("Hello update Items 1 run before return")
    if db_item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    for field, value in item.model_dump().items():
        setattr(db_item, field, value)

    db.commit()
    db.refresh(db_item)

    print("Hello update run before return")
    return db_item


# ==========================================
# DELETE
# ==========================================

@app.delete("/items/{item_id}")
def delete_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = (
        db.query(models.Item)
        .filter(models.Item.id == item_id)
        .first()
    )

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    db.delete(item)
    db.commit()

    return {
        "message": "Item deleted successfully"
    }