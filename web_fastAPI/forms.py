from pydantic import BaseModel, EmailStr, SecretStr


class UserRegistration(BaseModel):
    """Данный клас - это форма, которая используется для обработки данных, вводимых пользователем при регистрации.
    Наследуется от BaseModel, что позволяет использовать функциональность Pydantic.
    Данная форма отображается на странице Регистрация."""

    last_name: str
    first_name: str
    patronymic: str
    phone_number: str
    email: EmailStr
    password: SecretStr
    confirm_password: SecretStr


