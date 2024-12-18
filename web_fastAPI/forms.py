from pydantic import BaseModel, EmailStr, SecretStr


class UserRegistration(BaseModel):
    last_name: str
    first_name: str
    patronymic: str
    phone_number: str
    email: EmailStr
    password: SecretStr
    confirm_password: SecretStr


