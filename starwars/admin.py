from django.contrib import admin
from .models import Character, Starship

@admin.register(Starship)
class StarshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'manufacturer', 'crew')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ('name', 'gender', 'birth_year', 'starship')
