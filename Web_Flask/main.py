from flask import Flask
from routers.main_menu import main_menu_routes
from routers.portfolio_menu import portfolio_menu_routes
from routers.registration import user_registration_routes
from flask_wtf.csrf import CSRFProtect
from config import SECRET_KEY
from db_cherepaha import db, init_db, User


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cherepaha.db'

init_db(app)

csrf = CSRFProtect(app)


app.register_blueprint(main_menu_routes)

app.register_blueprint(portfolio_menu_routes)

app.register_blueprint(user_registration_routes)

if __name__ == "__main__":
    app.run()
