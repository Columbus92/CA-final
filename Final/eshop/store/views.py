from django.shortcuts import render
from django.http import HttpResponse
from .models import Store
from django.shortcuts import redirect

def home(request):
    store = Store.objects.all()
    print(store[0].image)
    return render(request, 'home.html', {'store': store})


def apie(request):
    return render(request, 'apie.html')

def akcijos(request):
    return render(request, 'akcijos.html')
def prekiu_sarasas(request, tipas):
    store = Store.objects.filter(name__icontains=tipas)
    return render(request, 'prekiu_sarasas.html', {'store': store})


