from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import main_menu, portfolio_menu

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(main_menu.router)

app.include_router(portfolio_menu.router)
