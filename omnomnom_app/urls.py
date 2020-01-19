from django.urls import path
from . import views

urlpatterns = [
    path('', views.zlecenia_lista, name='zlecenia_lista'),
]