from .models import NoteCreate


notes = []


def create_note(note: NoteCreate):

    new_note = {
        "id": len(notes) + 1,
        "user_id": note.user_id,
        "project_id": note.project_id,
        "title": note.title,
        "content": note.content
    }

    notes.append(new_note)

    return new_note


def get_project_notes(
    project_id: int
):

    return [
        note
        for note in notes
        if note["project_id"] == project_id
    ]


def get_note(
    note_id: int
):

    for note in notes:

        if note["id"] == note_id:
            return note

    return None


def delete_note(
    note_id: int
):

    for note in notes:

        if note["id"] == note_id:

            notes.remove(note)

            return True

    return False