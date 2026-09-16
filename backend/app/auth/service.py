from .models import UserCreate, UserLogin


users = []



def register_user(user: UserCreate):

    # Check if email already exists
    for existing_user in users:
        if existing_user["email"] == user.email:
            return None

    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "password": user.password
    }

    users.append(new_user)

    return new_user



def login_user(user: UserLogin):

    for existing_user in users:

        if (
            existing_user["email"] == user.email
            and existing_user["password"] == user.password
        ):
            return existing_user

    return None