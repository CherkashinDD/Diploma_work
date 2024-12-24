from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

router = APIRouter()

env = Environment(loader=FileSystemLoader('templates'))


@router.get("/portfolio/architecture")
def read_architecture(request: Request):
    """Данная функция обрабатывает GET запрос поступающий на URL, получает HTML-шаблон, рендерит его
       с переданным контекстом, возвращает в виде HTML-ответа. Отображает страницу Архитектура."""
    template = env.get_template('architecture.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)


@router.get("/portfolio/improvement")
def read_improvement(request: Request):
    """Данная функция обрабатывает GET запрос поступающий на URL, получает HTML-шаблон, рендерит его
       с переданным контекстом, возвращает в виде HTML-ответа. Отображает страницу Благоустройство."""
    template = env.get_template('improvement.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)


@router.get("/portfolio/commercial_interiors")
def read_commercial_interiors(request: Request):
    """Данная функция обрабатывает GET запрос поступающий на URL, получает HTML-шаблон, рендерит его
       с переданным контекстом, возвращает в виде HTML-ответа. Отображает страницу Коммерческие интерьеры."""
    template = env.get_template('commercial_interiors.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)


@router.get("/portfolio/residential_interiors")
def read_residential_interiors(request: Request):
    """Данная функция обрабатывает GET запрос поступающий на URL, получает HTML-шаблон, рендерит его
       с переданным контекстом, возвращает в виде HTML-ответа. Отображает страницу Жилые интерьеры."""
    template = env.get_template('residential_interiors.html')
    return HTMLResponse(content=template.render(request=request), status_code=200)
