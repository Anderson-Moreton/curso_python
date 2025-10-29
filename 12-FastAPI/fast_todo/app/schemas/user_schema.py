from pydantic import BaseModel, EmailStr, Field

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="The user's email address")
    username: str = Field(..., min_length=3, max_length=50, description="The user's username")
    password: str = Field(..., min_length=6, description="The user's password")