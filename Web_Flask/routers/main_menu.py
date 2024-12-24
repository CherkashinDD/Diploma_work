from flask import Blueprint, render_template

main_menu_routes = Blueprint('main_menu', __name__)


@main_menu_routes.route("/")
def home_page():
    """Данная функция обрабатывает запрос URL, после рендеринга HTML-шаблона, возвращает пользователю главную страницу,
       на основе HTML-шаблона"""
    return render_template("home_page.html")


@main_menu_routes.route("/portfolio")
def portfolio():
    """Данная функция обрабатывает запрос URL, после рендеринга HTML-шаблона,
       возвращает пользователю страницу Портфолио, на основе HTML-шаблона"""
    return render_template("portfolio.html")


@main_menu_routes.route("/contacts")
def contacts():
    """Данная функция обрабатывает запрос URL, после рендеринга HTML-шаблона,
        возвращает пользователю страницу Контакты, на основе HTML-шаблона"""
    return render_template("contacts.html")


@main_menu_routes.route("/services")
def services():
    """Данная функция обрабатывает запрос URL, после рендеринга HTML-шаблона,
       возвращает пользователю страницу Услуги, на основе HTML-шаблона"""
    return render_template("services.html")
