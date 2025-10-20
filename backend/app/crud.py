from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select, or_, func
from . import models, schemas

def list_customers(db: Session, q: Optional[str] = None, city: Optional[str] = None,
                   active: Optional[bool] = None, limit: int = 50, offset: int = 0) -> List[models.Customer]:
    stmt = select(models.Customer)
    if q:
        pattern = f"%{q.lower()}%"
        stmt = stmt.where(or_(
            func.lower(models.Customer.name).like(pattern),
            func.lower(models.Customer.email).like(pattern),
            func.lower(models.Customer.city).like(pattern),
            func.lower(models.Customer.customer_number).like(pattern),
        ))
    if city:
        stmt = stmt.where(func.lower(models.Customer.city) == city.lower())
    if active is not None:
        stmt = stmt.where(models.Customer.active == active)
    stmt = stmt.order_by(models.Customer.id).limit(limit).offset(offset)
    return db.execute(stmt).scalars().all()

def get_customer(db: Session, customer_id: int):
    return db.get(models.Customer, customer_id)

def create_customer(db: Session, data: schemas.CustomerCreate):
    obj = models.Customer(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_customer(db: Session, customer_id: int, data: schemas.CustomerUpdate):
    obj = get_customer(db, customer_id)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_customer(db: Session, customer_id: int) -> bool:
    obj = get_customer(db, customer_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
