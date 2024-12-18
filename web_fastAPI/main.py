from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import main_menu, portfolio_menu, user_registration

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(main_menu.router)

app.include_router(portfolio_menu.router)

app.include_router(user_registration.router)