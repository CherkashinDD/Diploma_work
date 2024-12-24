from flask import Blueprint, render_template

portfolio_menu_routes = Blueprint('portfolio_menu', __name__)


@portfolio_menu_routes.route("/portfolio/architecture")
def architecture():
    """Данная функция обрабатывает запрос URL, после рендеринга HTML-шаблона,
       возвращает пользователю страницу Архитектура, на основе HTML-шаблона"""
    return render_template("architecture.html")


@portfolio_menu_routes.route("/portfolio/improvement")
def improvement():
    """Данная функция обрабатывает запрос URL, после рендеринга HTML-шаблона,
       возвращает пользователю страницу Благоустройство, на основе HTML-шаблона"""
    return render_template("improvement.html")


@portfolio_menu_routes.route("/portfolio/commercial_interiors")
def commercial_interiors():
    """Данная функция обрабатывает запрос URL, после рендеринга HTML-шаблона,
       возвращает пользователю страницу Коммерческие интерьеры, на основе HTML-шаблона"""
    return render_template("commercial_interiors.html")


@portfolio_menu_routes.route("/portfolio/residential_interiors")
def residential_interiors():
    """Данная функция обрабатывает запрос URL, после рендеринга HTML-шаблона,
       возвращает пользователю страницу Коммерческие интерьеры, на основе HTML-шаблона"""
    return render_template("residential_interiors.html")
