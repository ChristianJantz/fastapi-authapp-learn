from ..models.users import BaseUser

class UserSchema(BaseUser):
    password: str