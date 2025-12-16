# starwars/views.py
from django.shortcuts import render, get_object_or_404
from .models import Character, Starship

# 1. Страница со всеми персонажами (Главная)
def all_characters_view(request):
    """
    Отображает список всех персонажей.
    """
    characters = Character.objects.all()
    context = {
        'characters': characters,
        'title': 'Все Персонажи Галактики'
    }
    return render(request, 'starwars/all_characters.html', context)

# 2. Страница с информацией о конкретном персонаже
def character_detail_view(request, pk):
    """
    Отображает информацию о конкретном персонаже по его ID (pk).
    """
    # Получаем объект или выводим 404, если не найден
    character = get_object_or_404(Character, pk=pk)
    context = {
        'character': character,
        'title': f'Персонаж: {character.name}'
    }
    return render(request, 'starwars/character_detail.html', context)

# 3. Страница с информацией о конкретном корабле
def starship_detail_view(request, pk):
    """
    Отображает информацию о конкретном корабле по его ID (pk).
    """
    starship = get_object_or_404(Starship, pk=pk)
    context = {
        'starship': starship,
        'title': f'Корабль: {starship.name}'
    }
    return render(request, 'starwars/starship_detail.html', context)