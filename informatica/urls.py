from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='informatica-home'),
    path('automatizacion/', views.automatizacion, name='informatica-automatizacion'),
    path('tareas/', views.tareas, name='informatica-tareas'),
]