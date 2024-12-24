from django import forms
from phonenumber_field.modelfields import PhoneNumberField


class UserRegistrer(forms.Form):
    """Данный клас - это форма, которая используется для обработки данных, вводимых пользователем при регистрации.
    Наследуется от forms.Form, что позволяет использовать функциональность Django, для работы с формами.
    Данная форма отображается на странице Регистрация."""

    last_name = forms.CharField(max_length=30, label='Введите фамилию')
    first_name = forms.CharField(max_length=30, label='last_name')
    patronymic = forms.CharField(max_length=30, label='Введите фамилию')
    phone_number = PhoneNumberField(label='Введите номер телефона', required=False)
    email = forms.EmailField(max_length=254, label='Введите email')
    password = forms.CharField(min_length=8, label='Введите пароль', strip=False, widget=forms.PasswordInput)
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль', strip=False, widget=forms.PasswordInput)
    subscribe = forms.BooleanField(required=False, label='Зарегистрироваться')
