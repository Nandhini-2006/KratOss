from fastapi import APIRouter, HTTPException

from .models import ProfileUpdate
from .service import (
    get_profile,
    update_profile
)


router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.get("/{user_id}")
def profile_details(
    user_id: int
):

    profile = get_profile(
        user_id
    )

    if profile is None:

        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    return {
        "profile": profile
    }


@router.put("/{user_id}")
def edit_profile(
    user_id: int,
    profile_data: ProfileUpdate
):

    profile = update_profile(
        user_id,
        profile_data
    )

    if profile is None:

        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    return {
        "message": "Profile updated successfully",
        "profile": profile
    }