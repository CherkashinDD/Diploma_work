from django.shortcuts import render


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
