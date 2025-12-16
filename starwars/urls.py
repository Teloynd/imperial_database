from django.urls import path
from . import views


app_name = 'starwars'

urlpatterns = [
    path('', views.all_characters_view, name='all_characters'),
    path('character/<int:pk>/', views.character_detail_view, name='character_detail'),
    path('starship/<int:pk>/', views.starship_detail_view, name='starship_detail'),
]