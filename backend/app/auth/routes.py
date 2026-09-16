from fastapi import APIRouter, HTTPException
from .models import UserCreate, UserLogin
from .service import register_user, login_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup")
def signup(user: UserCreate):

    new_user = register_user(user)

    if new_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return {
        "message": "Account created successfully",
        "user": {
            "id": new_user["id"],
            "name": new_user["name"],
            "email": new_user["email"]
        }
    }



@router.post("/login")
def login(user: UserLogin):

    logged_user = login_user(user)

    if logged_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "message": "Login successful",
        "user": {
            "id": logged_user["id"],
            "name": logged_user["name"],
            "email": logged_user["email"]
        }
    }