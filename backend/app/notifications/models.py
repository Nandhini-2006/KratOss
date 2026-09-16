from pydantic import BaseModel


class NotificationCreate(BaseModel):
    user_id: int
    notification_type: str
    title: str
    message: str


class NotificationResponse(BaseModel):
    id: int
    user_id: int
    notification_type: str
    title: str
    message: str
    read: bool