# starwars/urls.py
from django.urls import path
from . import views

# В Django 2.0+ обязательно нужно указывать app_name для корректной работы 'reverse'
app_name = 'starwars'

urlpatterns = [
    # Главная страница: список всех персонажей
    path('', views.all_characters_view, name='all_characters'),

    # Страница конкретного персонажа. Используем pk (primary key) для идентификации
    path('character/<int:pk>/', views.character_detail_view, name='character_detail'),

    # Страница конкретного корабля
    path('starship/<int:pk>/', views.starship_detail_view, name='starship_detail'),
]