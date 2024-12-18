from django.shortcuts import render
from .models import User


def home_page(request):
    return render(request, 'home_page.html')


def portfolio(request):
    title = "Портфолио"
    return render(request, 'portfolio.html', {'title': title})


def architecture(request):
    title = "Архитектура"
    return render(request, 'architecture.html', {'title': title})


def improvement(request):
    title = "Благоустройство"
    return render(request, 'improvement.html', {'title': title})


def residential_interiors(request):
    title = "Жилые интерьеры"
    return render(request, 'residential_interiors.html', {'title': title})


def commercial_interiors(request):
    title = "Комерческие интерьеры"
    return render(request, 'commercial_interiors.html', {'title': title})


def services(request):
    title = "Услуги"
    return render(request, 'services.html', {'title': title})


def contacts(request):
    title = "Контакты"
    return render(request, 'contacts.html', {'title': title})


def user_registration(request):
    last_names = [user.last_name for user in User.objects.all()]
    first_names = [user.first_name for user in User.objects.all()]
    patronymics = [user.patronymic for user in User.objects.all()]
    info = {}
    if request.method == 'POST':
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        patronymic = request.POST.get('patronymic')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")

        if (
                password == repeat_password
                and last_name not in last_names
                and first_name not in first_names
                and patronymic not in patronymics
        ):
            User.objects.create(
                last_name=last_name, first_name=first_name, patronymic=patronymic,
                phone_number=phone_number, email=email
            )
            welcome = f'Приветствуем, {last_name}{first_name}{patronymic}! Вы успешно зарегестрировались'
            info['welkom'] = welcome

        elif password != repeat_password:
            error_password = "Пароли не совпадают"
            info['error_password'] = error_password
            if last_name in last_names and first_name in first_names and patronymic in patronymics:
                error_username = "Пользователь уже существует"
                info['error_username'] = error_username

        elif last_name in last_names and first_name in first_names and patronymic in patronymics:
            error_username = "Пользователь уже существует"
            info['error_username'] = error_username

    return render(request, 'user_registration.html', info)
