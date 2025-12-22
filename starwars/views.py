from django.shortcuts import render, get_object_or_404
from .models import Character, Starship

def all_characters_view(request):
    characters = Character.objects.all()
    context = {
        'characters': characters,
        'title': 'Все Персонажи Галактики'
    }
    return render(request, 'starwars/all_characters.html', context)


def character_detail_view(request, pk):    
    character = get_object_or_404(Character, pk=pk)
    context = {
        'character': character,
        'title': f'Персонаж: {character.name}'
    }
    return render(request, 'starwars/character_detail.html', context)


def starship_detail_view(request, pk):
    starship = get_object_or_404(Starship, pk=pk)
    context = {
        'starship': starship,
        'title': f'Корабль: {starship.name}'
    }
    return render(request, 'starwars/starship_detail.html', context)