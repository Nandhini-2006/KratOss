from fastapi import APIRouter, HTTPException

from .models import NoteCreate
from .service import (
    create_note,
    get_project_notes,
    get_note,
    delete_note
)


router = APIRouter(
    prefix="/dev-notes",
    tags=["Developer Notes"]
)


@router.post("/")
def add_note(
    note: NoteCreate
):

    result = create_note(note)

    return {
        "message": "Note created successfully",
        "note": result
    }


@router.get("/project/{project_id}")
def project_notes(
    project_id: int
):

    return {
        "project_id": project_id,
        "notes": get_project_notes(
            project_id
        )
    }


@router.get("/{note_id}")
def note_details(
    note_id: int
):

    note = get_note(note_id)

    if note is None:

        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return note


@router.delete("/{note_id}")
def remove_note(
    note_id: int
):

    deleted = delete_note(
        note_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return {
        "message": "Note deleted successfully"
    }