from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apie/', views.apie, name='apie'),
    path('akcijos/', views.akcijos, name='akcijos'),
    path('prekiu_sarasas/<str:tipas>', views.prekiu_sarasas, name='prekiu_sarasas'),
]

