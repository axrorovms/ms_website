from django.urls import path
from .views import home, about, portfolio, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact')
]
