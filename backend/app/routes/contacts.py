from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db
from schemas.models import DeleteContactResponse, Contact, UpdateContact
from utils.contacts_crud import (
    contact_create,
    contact_delete,
    contact_get_one,
    contact_update,
    contact_get_all,
)

router = APIRouter(tags=["contacts"])


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=Contact)
def create_contact(contact: Contact, db: Session = Depends(get_db)):
    return contact_create(db=db, contact=contact)


@router.get("/list/all", status_code=status.HTTP_200_OK, response_model=List[Contact])
def get_all_contacts(db: Session = Depends(get_db)):
    return contact_get_all(db=db)


@router.get("/get/{id}", status_code=status.HTTP_200_OK, response_model=Contact)
def get_one_contact(id, db: Session = Depends(get_db)):
    return contact_get_one(db=db, id=id)


@router.delete(
    "/delete/{id}", status_code=status.HTTP_200_OK, response_model=DeleteContactResponse
)
def delete_contact(id, db: Session = Depends(get_db)):
    delete_status = contact_delete(db=db, id=id)
    if delete_status.detail == "Doesnt Exist":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found"
        )
    else:
        return delete_status
@router.patch("/update", status_code=status.HTTP_200_OK, response_model=Contact)
def update_contact(post: UpdateContact, db: Session = Depends(get_db)):
    return contact_update(db=db, contact=post)
