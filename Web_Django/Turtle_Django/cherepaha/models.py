from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(models.Model):
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество')
    phone_number = PhoneNumberField(null=True, blank=True, verbose_name='Номер телефона')
    email = models.EmailField(max_length=254, verbose_name='Email')


    def __str__(self):
        return self.first_name
