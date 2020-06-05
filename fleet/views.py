from django.shortcuts import render, HttpResponse
from .models import Car

# Create your views here.


def lista(request):
    car = Car.objects.all()
    return render(request, "lista.html", {
        "cars": car
    })


def pojazd(request, id):
    return render(request, 'pojazd.html', {
        'id_pojazdu': id
    })