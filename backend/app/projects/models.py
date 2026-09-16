from pydantic import BaseModel, HttpUrl
from typing import Optional


class ProjectCreate(BaseModel):
    name: str
    repo_url: HttpUrl


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    repo_url: Optional[HttpUrl] = None
    status: Optional[str] = None


class ProjectResponse(BaseModel):
    id: int
    name: str
    repo_url: str
    status: str