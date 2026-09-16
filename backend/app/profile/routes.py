from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from . import models
from . import service
from app.database.database import get_db

router = APIRouter(
    prefix="/profile",
    tags=["Profile and Security"]
)

@router.get("/{user_id}", response_model=models.ProfileResponse)
def get_profile(user_id: int, db: Session = Depends(get_db)):
    profile = service.get_profile(db, user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.put("/{user_id}", response_model=models.ProfileResponse)
def update_profile(user_id: int, profile_data: models.ProfileUpdate, db: Session = Depends(get_db)):
    profile = service.update_profile(db, user_id, profile_data)
    return profile

# Password Management
@router.post("/{user_id}/password/change")
def change_password(user_id: int, passwords: models.PasswordChangeRequest, db: Session = Depends(get_db)):
    return service.change_password(db, user_id, passwords)

@router.post("/password/reset")
def reset_password(req: models.PasswordResetRequest, db: Session = Depends(get_db)):
    # In reality, this would send an email and not require user_id in path
    return {"message": "Password reset link sent to email"}

# Security Keys & Passkeys
@router.post("/{user_id}/passkeys/register", response_model=models.PasskeyResponse)
def register_passkey(user_id: int, req: models.PasskeyRegisterRequest, db: Session = Depends(get_db)):
    return service.register_passkey(db, user_id, req)

@router.get("/{user_id}/passkeys")
def list_passkeys(user_id: int, db: Session = Depends(get_db)):
    return service.list_passkeys(db, user_id)

@router.delete("/{user_id}/passkeys/{passkey_id}")
def remove_passkey(user_id: int, passkey_id: int, db: Session = Depends(get_db)):
    return service.remove_passkey(db, user_id, passkey_id)

# MFA (TOTP)
@router.post("/{user_id}/mfa/totp/enable", response_model=models.TotpEnableResponse)
def enable_totp(user_id: int, db: Session = Depends(get_db)):
    return service.enable_totp(db, user_id)

@router.post("/{user_id}/mfa/totp/verify")
def verify_totp(user_id: int, req: models.TotpVerifyRequest, db: Session = Depends(get_db)):
    res = service.verify_totp(db, user_id, req)
    if not res.get("valid"):
        raise HTTPException(status_code=400, detail="Invalid TOTP code")
    return {"message": "TOTP verified"}

@router.post("/{user_id}/mfa/totp/disable")
def disable_totp(user_id: int, db: Session = Depends(get_db)):
    return service.disable_totp(db, user_id)

# OTP SMS/WhatsApp
@router.post("/{user_id}/mfa/otp/request")
def request_otp(user_id: int, req: models.OtpRequest, db: Session = Depends(get_db)):
    return service.request_otp(db, user_id, req)

@router.post("/{user_id}/mfa/otp/verify")
def verify_otp(user_id: int, req: models.OtpVerifyRequest, db: Session = Depends(get_db)):
    res = service.verify_otp(db, user_id, req)
    if not res.get("valid"):
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")
    return {"message": "OTP verified successfully"}

# Sessions
@router.get("/{user_id}/sessions")
def list_sessions(user_id: int, db: Session = Depends(get_db)):
    return service.list_sessions(db, user_id)

@router.delete("/{user_id}/sessions/{session_id}")
def logout_session(user_id: int, session_id: int, db: Session = Depends(get_db)):
    return service.logout_session(db, user_id, session_id)

@router.delete("/{user_id}/sessions")
def logout_all_sessions(user_id: int, db: Session = Depends(get_db)):
    return service.logout_all_sessions(db, user_id)

# Login Connections
@router.get("/{user_id}/connections")
def list_connections(user_id: int, db: Session = Depends(get_db)):
    return service.list_connections(db, user_id)

# Advanced Security Settings
@router.put("/{user_id}/security")
def update_security_settings(user_id: int, req: models.SecuritySettingsUpdate, db: Session = Depends(get_db)):
    return service.update_security_settings(db, user_id, req)

# Device code Auth
@router.post("/auth/device/start", response_model=models.DeviceCodeStartResponse)
def start_device_code(db: Session = Depends(get_db)):
    return service.start_device_code(db)

@router.post("/auth/device/verify")
def verify_device_code(req: models.DeviceCodeVerifyRequest, db: Session = Depends(get_db)):
    # Dummy verification
    if req.user_code == "ABCD-1234":
        return {"message": "Device authenticated successfully"}
    raise HTTPException(status_code=400, detail="Invalid user code")