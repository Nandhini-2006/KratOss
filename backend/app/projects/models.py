from pydantic import BaseModel, HttpUrl


class ProjectCreate(BaseModel):
    name: str
    repo_url: HttpUrl


class ProjectResponse(BaseModel):
    id: int
    name: str
    repo_url: str
    status: str