from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import db_models as dbm
from . import models as pydantic_models
import uuid
from datetime import datetime, timedelta

def get_profile(db: Session, user_id: int):
    return db.query(dbm.UserProfile).filter(dbm.UserProfile.user_id == user_id).first()

def update_profile(db: Session, user_id: int, profile_data: pydantic_models.ProfileUpdate):
    profile = get_profile(db, user_id)
    if not profile:
        profile = dbm.UserProfile(user_id=user_id)
        db.add(profile)
    
    if profile_data.first_name is not None:
        profile.first_name = profile_data.first_name
    if profile_data.last_name is not None:
        profile.last_name = profile_data.last_name
    if profile_data.avatar_url is not None:
        profile.avatar_url = profile_data.avatar_url
        
    db.commit()
    db.refresh(profile)
    return profile

def change_password(db: Session, user_id: int, passwords: pydantic_models.PasswordChangeRequest):
    cred = db.query(dbm.PasswordCredential).filter(dbm.PasswordCredential.user_id == user_id).first()
    if not cred:
        cred = dbm.PasswordCredential(user_id=user_id, hashed_password="hashed_" + passwords.new_password)
        db.add(cred)
    else:
        cred.hashed_password = "hashed_" + passwords.new_password
        cred.last_changed = datetime.utcnow()
    db.commit()
    return {"message": "Password changed successfully"}

def register_passkey(db: Session, user_id: int, passkey: pydantic_models.PasskeyRegisterRequest):
    db_passkey = dbm.Passkey(
        user_id=user_id,
        credential_id=str(uuid.uuid4()),
        public_key=passkey.public_key,
        name=passkey.name
    )
    db.add(db_passkey)
    db.commit()
    db.refresh(db_passkey)
    return db_passkey

def list_passkeys(db: Session, user_id: int):
    return db.query(dbm.Passkey).filter(dbm.Passkey.user_id == user_id).all()

def remove_passkey(db: Session, user_id: int, passkey_id: int):
    db_passkey = db.query(dbm.Passkey).filter(dbm.Passkey.id == passkey_id, dbm.Passkey.user_id == user_id).first()
    if db_passkey:
        db.delete(db_passkey)
        db.commit()
    return {"message": "Passkey removed"}

def enable_totp(db: Session, user_id: int):
    mfa = db.query(dbm.MfaSetting).filter(dbm.MfaSetting.user_id == user_id).first()
    if not mfa:
        mfa = dbm.MfaSetting(user_id=user_id)
        db.add(mfa)
    
    mfa.totp_secret = "generated_secret_here"
    mfa.is_totp_enabled = True
    db.commit()
    return {"secret": mfa.totp_secret, "qr_code_url": f"otpauth://totp/KratOss?secret={mfa.totp_secret}"}

def verify_totp(db: Session, user_id: int, req: pydantic_models.TotpVerifyRequest):
    # Dummy verification
    if req.code == "123456":
        return {"valid": True}
    return {"valid": False}

def disable_totp(db: Session, user_id: int):
    mfa = db.query(dbm.MfaSetting).filter(dbm.MfaSetting.user_id == user_id).first()
    if mfa:
        mfa.is_totp_enabled = False
        mfa.totp_secret = None
        db.commit()
    return {"message": "TOTP disabled"}

def request_otp(db: Session, user_id: int, req: pydantic_models.OtpRequest):
    otp = dbm.OtpCode(
        user_id=user_id,
        code="123456",
        expires_at=datetime.utcnow() + timedelta(minutes=10),
        channel=req.channel
    )
    db.add(otp)
    db.commit()
    return {"message": f"OTP sent via {req.channel}"}

def verify_otp(db: Session, user_id: int, req: pydantic_models.OtpVerifyRequest):
    otp = db.query(dbm.OtpCode).filter(dbm.OtpCode.user_id == user_id, dbm.OtpCode.channel == req.channel).order_by(dbm.OtpCode.id.desc()).first()
    if otp and otp.code == req.code and not otp.is_used and otp.expires_at > datetime.utcnow():
        otp.is_used = True
        db.commit()
        return {"valid": True}
    return {"valid": False}

def list_sessions(db: Session, user_id: int):
    return db.query(dbm.Session).filter(dbm.Session.user_id == user_id, dbm.Session.is_active == True).all()

def logout_session(db: Session, user_id: int, session_id: int):
    session = db.query(dbm.Session).filter(dbm.Session.id == session_id, dbm.Session.user_id == user_id).first()
    if session:
        session.is_active = False
        db.commit()
    return {"message": "Session logged out"}

def logout_all_sessions(db: Session, user_id: int):
    db.query(dbm.Session).filter(dbm.Session.user_id == user_id).update({"is_active": False})
    db.commit()
    return {"message": "All sessions logged out"}

def list_connections(db: Session, user_id: int):
    return db.query(dbm.LoginConnection).filter(dbm.LoginConnection.user_id == user_id).all()

def update_security_settings(db: Session, user_id: int, req: pydantic_models.SecuritySettingsUpdate):
    sec = db.query(dbm.SecuritySetting).filter(dbm.SecuritySetting.user_id == user_id).first()
    if not sec:
        sec = dbm.SecuritySetting(user_id=user_id)
        db.add(sec)
    
    if req.lockdown_mode is not None:
        sec.lockdown_mode = req.lockdown_mode
    if req.developer_mode is not None:
        sec.developer_mode = req.developer_mode
    if req.csp_enforcement_level is not None:
        sec.csp_enforcement_level = req.csp_enforcement_level
        
    db.commit()
    db.refresh(sec)
    return sec

def start_device_code(db: Session):
    return {
        "device_code": str(uuid.uuid4()),
        "user_code": "ABCD-1234",
        "verification_uri": "https://kratos.app/device",
        "expires_in": 900
    }