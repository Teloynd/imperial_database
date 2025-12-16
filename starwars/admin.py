from django.contrib import admin
from .models import Character, Starship

@admin.register(Starship)
class StarshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'manufacturer', 'crew')
    search_fields = ('name', 'model')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'birth_year', 'starship') 
    list_filter = ('gender', 'birth_year') 
    search_fields = ('name',) 
    fieldsets = (
        (None, {'fields': ('name', 'gender', 'birth_year', 'starship')}),
        ('Физические характеристики', {'fields': ('height', 'mass', 'hair_color', 'skin_color', 'eye_color')}),
    )