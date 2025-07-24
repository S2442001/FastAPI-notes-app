from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.notes import NoteCreate, NoteUpdate, NoteOut
from app.crud import notes
from app.core.security  import get_current_user
from app.database import get_db
from app.models import models

router = APIRouter(prefix="/notes", tags=["Notes"])

# Create Note
@router.post("/", response_model=NoteOut)
def create_note(note: NoteCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return notes.create_note(db, note, user_id=current_user.id)

# Get All Notes
@router.get("/", response_model=list[NoteOut])
def read_notes(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return notes.get_user_notes(db, user_id=current_user.id)

# Get Single Note
@router.get("/{note_id}", response_model=NoteOut)
def read_note(note_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    note = notes.get_note_by_id(db, note_id, current_user.id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

# Update Note
@router.put("/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note_data: NoteUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    note = notes.update_note(db, note_id, note_data, current_user.id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found or unauthorized")
    return note

# Delete Note
@router.delete("/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    success = notes.delete_note(db, note_id, current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found or unauthorized")
    return {"detail": "Note deleted"}
