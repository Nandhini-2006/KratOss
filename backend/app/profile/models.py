from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# Profile
class ProfileUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar_url: Optional[str] = None

class ProfileResponse(BaseModel):
    id: int
    user_id: int
    first_name: Optional[str]
    last_name: Optional[str]
    avatar_url: Optional[str]

# Password
class PasswordChangeRequest(BaseModel):
    old_password: str
    new_password: str

class PasswordResetRequest(BaseModel):
    email: EmailStr

# Passkeys
class PasskeyRegisterRequest(BaseModel):
    name: str
    public_key: str

class PasskeyResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

# MFA (TOTP)
class TotpVerifyRequest(BaseModel):
    code: str

class TotpEnableResponse(BaseModel):
    secret: str
    qr_code_url: str

# MFA (OTP SMS/WhatsApp)
class OtpRequest(BaseModel):
    channel: str # SMS or WhatsApp
    phone_number: str

class OtpVerifyRequest(BaseModel):
    code: str
    channel: str

# Sessions
class SessionResponse(BaseModel):
    id: int
    device_info: Optional[str]
    ip_address: Optional[str]
    created_at: datetime
    is_active: bool

# Login Connections
class LoginConnectionResponse(BaseModel):
    id: int
    provider: str
    connected_at: datetime

# Security Settings
class SecuritySettingsUpdate(BaseModel):
    lockdown_mode: Optional[bool] = None
    developer_mode: Optional[bool] = None
    csp_enforcement_level: Optional[str] = None

class SecuritySettingsResponse(BaseModel):
    lockdown_mode: bool
    developer_mode: bool
    csp_enforcement_level: str

# Device code
class DeviceCodeStartResponse(BaseModel):
    device_code: str
    user_code: str
    verification_uri: str
    expires_in: int

class DeviceCodeVerifyRequest(BaseModel):
    user_code: str