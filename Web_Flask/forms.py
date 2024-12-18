from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from phonenumbers import is_valid_number, parse


class UserRegister(FlaskForm):
    last_name = StringField('Введите фамилию', validators=[DataRequired(), Length(max=30)])
    first_name = StringField('Введите имя', validators=[DataRequired(), Length(max=30)])
    patronymic = StringField('Введите отчество', validators=[DataRequired(), Length(max=30)])
    phone_number = StringField('Введите номер телефона', validators=[Length(max=15)])
    email = EmailField('Введите email', validators=[DataRequired(), Email(), Length(max=254)])
    password = PasswordField('Введите пароль', validators=[DataRequired(), Length(min=8)])
    repeat_password = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    subscribe = BooleanField('Зарегистрироваться')

    def validate_phone_number(self, field):
        try:
            phone_number = parse(field.data, None)
            if not is_valid_number(phone_number):
                raise ValueError('Недопустимый номер телефона')
        except Exception:
            raise ValueError('Недопустимый номер телефона')