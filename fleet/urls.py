from django.urls import path

from .views import *

urlpatterns = [
    path('', lista),
    path('<int:id>', pojazd)
]