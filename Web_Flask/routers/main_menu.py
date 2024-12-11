from flask import Blueprint, render_template

main_menu_routes = Blueprint('main_menu', __name__)


@main_menu_routes.route("/")
def home_page():
    return render_template("home_page.html")


@main_menu_routes.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@main_menu_routes.route("/contacts")
def contacts():
    return render_template("contacts.html")


@main_menu_routes.route("/services")
def services():
    return render_template("services.html")
