from pydantic import BaseModel


class NoteCreate(BaseModel):
    user_id: int
    project_id: int
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    user_id: int
    project_id: int
    title: str
    content: str