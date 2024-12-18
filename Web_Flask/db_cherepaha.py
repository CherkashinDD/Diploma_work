from flask_sqlalchemy import SQLAlchemy
from phonenumbers import parse, is_valid_number



db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(100), nullable=False, info={'label': 'Фамилия'})
    first_name = db.Column(db.String(100), nullable=False, info={'label': 'Имя'})
    patronymic = db.Column(db.String(100), nullable=False, info={'label': 'Отчество'})
    phone_number = db.Column(db.String(15), nullable=True, info={'label': 'Номер телефона'})
    email = db.Column(db.String(254), nullable=False, info={'label': 'Email'})

    def __repr__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def validate_phone_number(self):
        if not hasattr(self, 'phone_number'):
            raise AttributeError('Введите номер телефона')
        try:
            phone_number = parse(self.phone_number, None)
            if not is_valid_number(phone_number):
                raise ValueError('Недопустимый номер телефона')
        except Exception as e:
            raise ValueError(f'Недопустимый номер телефона: {str(e)}')


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()



