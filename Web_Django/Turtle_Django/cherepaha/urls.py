from django.urls import path
from cherepaha.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/architecture/', architecture, name='architecture'),
    path('portfolio/improvement/', improvement, name='improvement'),
    path('portfolio/residential_interiors/', residential_interiors, name='residential_interiors'),
    path('portfolio/commercial_interiors/', commercial_interiors, name='commercial_interiors'),
    path('services/', services, name='services'),
    path('contacts/', contacts, name='contacts'),
    path('user_registration/', user_registration, name='user_registration')
]