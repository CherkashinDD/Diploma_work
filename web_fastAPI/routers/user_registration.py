from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
from db_cherepaha import session, User

router = APIRouter()

env = Environment(loader=FileSystemLoader('templates'))


@router.get("/user_registration")
def read_user_registration(request: Request):
    """Данная функция обрабатывает GET запрос поступающий на URL, получает HTML-шаблон, рендерит его
       с переданным контекстом, возвращает в виде HTML-ответа. Отображает страницу Регистрация."""

    template = env.get_template('user_registration.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)


@router.post("/user_registration")
def create_user_registration(
        last_name: str = Form(...),
        first_name: str = Form(...),
        patronymic: str = Form(...),
        phone_number: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        confirm_password: str = Form(...)
):
    """Данная функция обрабатывает POST запросы поступающие на URL, для отправки данных. Принимает параметр,
       которые отражены в форме. Все параметры обязательны для заполнения. Проводит проверку на совпадение паролей,
       проверяет на наличие создаваемого пользователя в базе данных. Если все проверки пройдены,
       создаёт новый объект класса User с переданными данными. Пытается добавить пользователя в сессию базы данных
       cherepaha.db и зафиксировать изменения. При успхе, формируется сообщение об успешной регистрации.
       В противном случае формирует сообщение о причинах неудачи. Возвращает соответствующий HTML ответ,
       в зависимости от результата операции. Результатом неудачи может быть не совпадение паролей
        или полное совпадение фамилии, имиени, отчества в базе данных"""

    if password != confirm_password:
        return HTMLResponse(
            content=env.get_template('user_registration.html').render(request=None, error="Пароли не совпадают"),
            status_code=400
        )

    existing_user = session.query(User).filter_by(
        last_name=last_name,
        first_name=first_name,
        patronymic=patronymic
    ).first()
    if existing_user:
        return HTMLResponse(
            content=env.get_template('user_registration.html').render(request=None,
                                                                      error="Такой пользователь уже существует"),
            status_code=400
        )

    user = User(
        last_name=last_name,
        first_name=first_name,
        patronymic=patronymic,
        phone_number=phone_number,
        email=email
    )

    try:
        session.add(user)
        session.commit()
        message = f"{last_name} {first_name} {patronymic} успешно зарегистрировался(лась)"
        return HTMLResponse(
            content=env.get_template('user_registration.html').render(request=None, message=message),
            status_code=200
        )
    except Exception as e:
        session.rollback()
        return HTMLResponse(
            content=env.get_template('user_registration.html').render(request=None, error=str(e)),
            status_code=400
        )
