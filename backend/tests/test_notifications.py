from app.notifications.models import (
    NotificationCreate
)

from app.notifications.service import (
    create_notification
)


def test_notification():

    notification = NotificationCreate(
        user_id=1,
        notification_type="HIGH_RISK",
        title="High Risk Detected",
        message="A high-risk crypto asset was found."
    )

    result = create_notification(
        notification
    )

    assert result["user_id"] == 1
    assert result["read"] is False