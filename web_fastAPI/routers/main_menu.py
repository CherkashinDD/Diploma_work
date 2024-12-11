from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Template, Environment, FileSystemLoader

router = APIRouter()

env = Environment(loader=FileSystemLoader('templates'))


@router.get("/")
def read_home_page():
    with open("templates/home_page.html", "r", encoding="utf-8") as f:
        template = Template(f.read())
    return HTMLResponse(content=template.render(request={"path": "/"}), status_code=200)


@router.get("/portfolio")
def read_portfolio(request: Request):
    template = env.get_template('portfolio.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)


@router.get("/contacts")
def read_contacts():
    with open("templates/contacts.html", "r", encoding="utf-8") as f:
        template = Template(f.read())
    return HTMLResponse(content=template.render(request={"path": "/contacts"}), status_code=200)


@router.get("/services")
def read_services(request: Request):
    template = env.get_template('services.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)
