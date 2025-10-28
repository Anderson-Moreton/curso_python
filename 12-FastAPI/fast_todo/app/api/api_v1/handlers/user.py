from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/test")
async def test_user():
    return {"message": "User endpoint is working!"}