from pydantic import BaseModel
from typing import Optional


class ApplicantCreate(BaseModel):

    name: str

    email: Optional[str] = None

    phone: Optional[str] = None

    country: str = "India"

    education: Optional[str] = None

    field: Optional[str] = None

    target: Optional[str] = None


class ApplicantResponse(ApplicantCreate):

    id: int

    class Config:
        from_attributes = True