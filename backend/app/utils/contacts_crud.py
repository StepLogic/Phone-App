from uuid import UUID

from sqlalchemy.orm import Session

from database.models import Contacts
from schemas.models import DeleteContactResponse, Contact, UpdateContact


def contact_create(db: Session, contact: Contact):
    db_contact = Contacts(first_name=contact.first_name, last_name=contact.last_name,phone=contact.phone)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def contact_get_all(db: Session):
    return db.query(Contacts).all()


def contact_get_one(db: Session, id: UUID):
    return db.query(Contacts).filter_by(id=id).one()


def contact_update(db: Session, contact: UpdateContact):
    update_query = {Contacts.first_name: contact.title, Contacts.last_name: contact.description}
    db.query(Contacts).filter_by(id=contact.id).update(update_query)
    db.commit()
    return db.query(Contacts).filter_by(id=contact.id).one()


def contact_delete(db: Session, id: UUID):
    post = db.query(Contacts).filter_by(id=id).all()
    if not post:
        return DeleteContactResponse(detail="Doesnt Exist")
    db.query(Contacts).filter_by(id=id).delete()
    db.commit()
    return DeleteContactResponse(detail="Post Deleted")
