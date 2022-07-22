from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class Contact(BaseModel):
    id: Optional[UUID]
    first_name: str
    last_name: str
    phone :str
    class Config:
        orm_mode = True


class DeleteContactResponse(BaseModel):
    detail: str


class UpdateContact(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    phone :str
    class Config:
        orm_mode = True
