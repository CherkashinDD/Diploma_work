from flask import Flask
from routers.main_menu import main_menu_routes
from routers.portfolio_menu import portfolio_menu_routes

app = Flask(__name__)

app.register_blueprint(main_menu_routes, url_perfix='/main_menu')

app.register_blueprint(portfolio_menu_routes, url_perfix='/portfolio_menu')

if __name__ == "__main__":
    app.run()
