from .models import ProfileUpdate


profiles = []


def create_profile(
    user_id: int,
    name: str,
    email: str
):

    profile = {
        "id": user_id,
        "name": name,
        "email": email
    }

    profiles.append(profile)

    return profile


def get_profile(
    user_id: int
):

    for profile in profiles:

        if profile["id"] == user_id:
            return profile

    return None


def update_profile(
    user_id: int,
    profile_data: ProfileUpdate
):

    for profile in profiles:

        if profile["id"] == user_id:

            profile["name"] = profile_data.name
            profile["email"] = profile_data.email

            return profile

    return None