from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Данный класс является моделью базы данныхcherepaha.db., которая создаёт таблицу users.
       Наследуется от db.Model, что позволяет использовать функциональность, предоставляемую SQLAlchemy,
       для работы с базами данных"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(100), nullable=False, info={'label': 'Фамилия'})
    first_name = db.Column(db.String(100), nullable=False, info={'label': 'Имя'})
    patronymic = db.Column(db.String(100), nullable=False, info={'label': 'Отчество'})
    phone_number = db.Column(db.String(15), nullable=True, info={'label': 'Номер телефона'})
    email = db.Column(db.String(254), nullable=False, info={'label': 'Email'})

    def __repr__(self):
        """Данный метод определяет строковое представление объекта User,
           для удобства вывода информации о пользователе"""

        return f"{self.last_name} {self.first_name} {self.patronymic}"


def init_db(app):
    """Данная функция принимает в качестве аргумента объект приложения Flask, что позволяет  SQLAlchemy использовать
       настройки и контекст приложения для работы с базой данных. Создаёт контекст приложения,
       который позволит получить доступ к текущему приложению и его конфигурации,
       что необходимо для работы с базой данных. Создаёт таблицу в базе данных (если она ещё не существует),
        определённую моделью User. Функция служит для настройки и нициализации базы данных при запуске приложения."""

    db.init_app(app)
    with app.app_context():
        db.create_all()
