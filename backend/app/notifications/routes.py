from fastapi import APIRouter, HTTPException

from .models import NotificationCreate
from .service import (
    create_notification,
    get_user_notifications,
    mark_as_read
)


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.post("/")
def add_notification(
    notification: NotificationCreate
):

    result = create_notification(
        notification
    )

    return {
        "message": "Notification created",
        "notification": result
    }


@router.get("/{user_id}")
def get_notifications(
    user_id: int
):

    return {
        "user_id": user_id,
        "notifications": get_user_notifications(
            user_id
        )
    }


@router.patch("/{notification_id}/read")
def read_notification(
    notification_id: int
):

    notification = mark_as_read(
        notification_id
    )

    if notification is None:

        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return {
        "message": "Notification marked as read",
        "notification": notification
    }