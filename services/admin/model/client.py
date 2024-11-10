from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Optional role validation using Enum (Optional, if you know the specific roles)
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    user = "user"

class ClientModel(BaseModel):
    name: Optional[str] = None
    mail: Optional[EmailStr] = None
    password: Optional[str] = None  # Password should be a string
    role: Optional[RoleEnum] = None  # Using Enum for roles
    createdAt: Optional[datetime] = None  # Use datetime for createdAt
    updateAt: Optional[datetime] = None  # Use datetime for updatedAt

    class Config:
        # Ensure datetime is serialized to ISO 8601 format
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        }
