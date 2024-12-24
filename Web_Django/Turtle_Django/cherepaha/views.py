from django.shortcuts import render
from .models import User


def home_page(request):
    """Данная функция принимает запрос, содержащий информацию о текущем HTML-запросе,
     и генерирует главную HTML-страницу"""
    return render(request, 'home_page.html')


def portfolio(request):
    """Данная функция принимает запрос, содержащий информацию о текущем HTML-запросе,
    и генерирует HTML-страницу Портфолио. Предаёт переменную title в шаблон (доступна как title)"""
    title = "Портфолио"
    return render(request, 'portfolio.html', {'title': title})


def architecture(request):
    """Данная функция принимает запрос, содержащий информацию о текущем HTML-запросе,
    и генерирует HTML-страницу Архитектура. Предаёт переменную title в шаблон (доступна как title)"""
    title = "Архитектура"
    return render(request, 'architecture.html', {'title': title})


def improvement(request):
    """Данная функция принимает запрос, содержащий информацию о текущем HTML-запросе,
    и генерирует HTML-страницу Благоустройство. Предаёт переменную title в шаблон (доступна как title)"""
    title = "Благоустройство"
    return render(request, 'improvement.html', {'title': title})


def residential_interiors(request):
    """Данная функция принимает запрос, содержащий информацию о текущем HTML-запросе,
    и генерирует HTML-страницу Жилые интерьеры. Предаёт переменную title в шаблон (доступна как title)"""
    title = "Жилые интерьеры"
    return render(request, 'residential_interiors.html', {'title': title})


def commercial_interiors(request):
    """Данная функция принимает запрос, содержащий информацию о текущем HTML-запросе,
    и генерирует HTML-страницу Комерческие интерьеры. Предаёт переменную title в шаблон (доступна как title)"""
    title = "Комерческие интерьеры"
    return render(request, 'commercial_interiors.html', {'title': title})


def services(request):
    """Данная функция принимает запрос, содержащий информацию о текущем HTML-запросе,
    и генерирует HTML-страницу Услуги. Предаёт переменную title в шаблон (доступна как title)"""
    title = "Услуги"
    return render(request, 'services.html', {'title': title})


def contacts(request):
    """Данная функция принимает запрос, содержащий информацию о текущем HTML-запросе,
    и генерирует HTML-страницу Контакты. Предаёт переменную title в шаблон (доступна как title)"""
    title = "Контакты"
    return render(request, 'contacts.html', {'title': title})


def user_registration(request):
    """Данная функция принимает запрос, содержащий информацию о текущем HTML-запросе.
    Гененрирует списки last_names, first_names, patronymics всех пользователей из базы данных.
    Если метод запроса -"POST", функция извлекает данные, отправленные через форму регистрации, и сохраняет
    их в соответствующие переменные. Проверяет совпадение паролей при регистрации.
    Проверяет существует ли пользователь. Пользователь будет создан только если совпадают пароли и если
    хотябы один из пораметров не совпадает (фамилия, имя, отчество).
    В словарь info сохраняются сообщения для пользователя. В случае успешной или не успешной регистрации
    пользователь получит соответствующее сообщение. В конце функция генерирует HTML-страницу Регистрация,
    передаёт словарь info для отображения сообщений пользователю.
    """
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
