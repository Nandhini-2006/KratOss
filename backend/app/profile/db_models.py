from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.database import Base

class ProfileUser(Base):
    """
    User model specifically created under profile as requested.
    If you already have a User in database/models.py, you may need to resolve the conflict later.
    """
    __tablename__ = "profile_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    profile = relationship("UserProfile", back_populates="user", uselist=False)
    preferences = relationship("UserPreference", back_populates="user", uselist=False)
    memory_settings = relationship("MemorySetting", back_populates="user", uselist=False)
    memory_summary = relationship("MemorySummary", back_populates="user", uselist=False)
    password_credentials = relationship("PasswordCredential", back_populates="user", uselist=False)
    passkeys = relationship("Passkey", back_populates="user")
    mfa_settings = relationship("MfaSetting", back_populates="user", uselist=False)
    mfa_recovery_codes = relationship("MfaRecoveryCode", back_populates="user")
    otp_codes = relationship("OtpCode", back_populates="user")
    sessions = relationship("Session", back_populates="user")
    login_connections = relationship("LoginConnection", back_populates="user")
    security_settings = relationship("SecuritySetting", back_populates="user", uselist=False)


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profile_users.id"), unique=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)

    user = relationship("ProfileUser", back_populates="profile")


class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profile_users.id"), unique=True)
    theme = Column(String, default="light")
    language = Column(String, default="en")
    notifications_enabled = Column(Boolean, default=True)

    user = relationship("ProfileUser", back_populates="preferences")


class MemorySetting(Base):
    __tablename__ = "memory_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profile_users.id"), unique=True)
    retention_days = Column(Integer, default=30)
    auto_clear = Column(Boolean, default=False)

    user = relationship("ProfileUser", back_populates="memory_settings")


class MemorySummary(Base):
    __tablename__ = "memory_summary"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profile_users.id"), unique=True)
    total_memories = Column(Integer, default=0)
    storage_used_bytes = Column(Integer, default=0)

    user = relationship("ProfileUser", back_populates="memory_summary")


class PasswordCredential(Base):
    __tablename__ = "password_credentials"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profile_users.id"), unique=True)
    hashed_password = Column(String, nullable=False)
    last_changed = Column(DateTime, default=datetime.utcnow)

    user = relationship("ProfileUser", back_populates="password_credentials")


class Passkey(Base):
    __tablename__ = "passkeys"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profile_users.id"))
    credential_id = Column(String, unique=True, index=True)
    public_key = Column(Text, nullable=False)
    sign_count = Column(Integer, default=0)
    name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("ProfileUser", back_populates="passkeys")


class MfaSetting(Base):
    __tablename__ = "mfa_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profile_users.id"), unique=True)
    is_totp_enabled = Column(Boolean, default=False)
    totp_secret = Column(String, nullable=True)
    is_sms_enabled = Column(Boolean, default=False)
    phone_number = Column(String, nullable=True)

    user = relationship("ProfileUser", back_populates="mfa_settings")


class MfaRecoveryCode(Base):
    __tablename__ = "mfa_recovery_codes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profile_users.id"))
    code_hash = Column(String, nullable=False)
    is_used = Column(Boolean, default=False)

    user = relationship("ProfileUser", back_populates="mfa_recovery_codes")


class OtpCode(Base):
    __tablename__ = "otp_codes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profile_users.id"))
    code = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    is_used = Column(Boolean, default=False)
    channel = Column(String) # e.g., "SMS", "WhatsApp"

    user = relationship("ProfileUser", back_populates="otp_codes")


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profile_users.id"))
    session_token = Column(String, unique=True, index=True)
    device_info = Column(String, nullable=True)
    ip_address = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)

    user = relationship("ProfileUser", back_populates="sessions")


class LoginConnection(Base):
    __tablename__ = "login_connections"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profile_users.id"))
    provider = Column(String, nullable=False) # e.g., "Google", "GitHub"
    provider_user_id = Column(String, nullable=False)
    connected_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("ProfileUser", back_populates="login_connections")


class SecuritySetting(Base):
    __tablename__ = "security_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("profile_users.id"), unique=True)
    lockdown_mode = Column(Boolean, default=False)
    developer_mode = Column(Boolean, default=False)
    csp_enforcement_level = Column(String, default="standard")

    user = relationship("ProfileUser", back_populates="security_settings")
