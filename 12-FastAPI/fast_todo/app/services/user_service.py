from schemas.user_schema import UserAuth
from models.user_model import User

class UserService:
    @staticmethod
    async def create_user(user: UserAuth) -> User:
        user = User(
            email=user.email,
            username=user.username,
            hash_password=user.password  # In a real app, hash the password!
        )
