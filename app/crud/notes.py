from sqlalchemy.orm import Session
from app.models.models import Note, User
from app.schemas.notes import NoteCreate, NoteUpdate

def create_note(db: Session, note_data: NoteCreate, user_id: int):
    note = Note(**note_data.dict(), user_id=user_id)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def get_user_notes(db: Session, user_id: int):
    return db.query(Note).filter(Note.user_id == user_id).all()

def get_note_by_id(db: Session, note_id: int, user_id: int):
    return db.query(Note).filter(Note.id == note_id, Note.user_id == user_id).first()

def update_note(db: Session, note_id: int, note_data: NoteUpdate, user_id: int):
    note = get_note_by_id(db, note_id, user_id)
    if not note:
        return None
    for field, value in note_data.dict(exclude_unset=True).items():
        setattr(note, field, value)
    db.commit()
    db.refresh(note)
    return note

def delete_note(db: Session, note_id: int, user_id: int):
    note = get_note_by_id(db, note_id, user_id)
    if not note:
        return False
    db.delete(note)
    db.commit()
    return True
