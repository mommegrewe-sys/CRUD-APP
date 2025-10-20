from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class CustomerBase(BaseModel):
    customer_number: Optional[str] = Field(None, max_length=32)
    name: str = Field(..., max_length=255)
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    street: Optional[str] = None
    postal_code: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = "Germany"
    active: Optional[bool] = True

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    customer_number: Optional[str] = Field(None, max_length=32)
    name: Optional[str] = Field(None, max_length=255)
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    street: Optional[str] = None
    postal_code: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    active: Optional[bool] = None

class CustomerOut(CustomerBase):
    id: int
    class Config:
        from_attributes = True
