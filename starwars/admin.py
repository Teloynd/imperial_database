# starwars/admin.py
from django.contrib import admin
from .models import Character, Starship

# Настройка для модели Starship
@admin.register(Starship)
class StarshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'manufacturer', 'crew')
    search_fields = ('name', 'model')

# Настройка для модели Character
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'birth_year', 'starship') # Отображаемые колонки
    list_filter = ('gender', 'birth_year') # Фильтры справа
    search_fields = ('name',) # Поиск по имени
    # Поля для отображения/редактирования на странице персонажа
    fieldsets = (
        (None, {'fields': ('name', 'gender', 'birth_year', 'starship')}),
        ('Физические характеристики', {'fields': ('height', 'mass', 'hair_color', 'skin_color', 'eye_color')}),
    )