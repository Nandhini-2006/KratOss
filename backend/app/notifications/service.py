from .models import NotificationCreate


notifications = []


def create_notification(
    notification: NotificationCreate
):

    new_notification = {
        "id": len(notifications) + 1,
        "user_id": notification.user_id,
        "notification_type": notification.notification_type,
        "title": notification.title,
        "message": notification.message,
        "read": False
    }

    notifications.append(
        new_notification
    )

    return new_notification


def get_user_notifications(
    user_id: int
):

    return [
        notification
        for notification in notifications
        if notification["user_id"] == user_id
    ]


def mark_as_read(
    notification_id: int
):

    for notification in notifications:

        if notification["id"] == notification_id:

            notification["read"] = True

            return notification

    return None