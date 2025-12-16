# starwars/models.py
from django.db import models

# Модель Корабля (Starship)
class Starship(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название Корабля")
    model = models.CharField(max_length=100, verbose_name="Модель")
    manufacturer = models.CharField(max_length=100, verbose_name="Производитель")
    
    # Теперь эти поля ОБЯЗАТЕЛЬНЫ для заполнения!
    crew = models.IntegerField(verbose_name="Экипаж") 
    passengers = models.IntegerField(verbose_name="Пассажиры")
    
    # DecimalField для чисел с плавающей точкой
    hyperdrive_rating = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Рейтинг гипердрайва")

    class Meta:
        verbose_name = "Корабль"
        verbose_name_plural = "Корабли"

    def __str__(self):
        return self.name

# Модель Персонажа (Character)
class Character(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Имя Персонажа")
    
    height = models.IntegerField(verbose_name="Рост (см)") 
    mass = models.IntegerField(verbose_name="Масса (кг)") 
    
    hair_color = models.CharField(max_length=50, verbose_name="Цвет волос")
    skin_color = models.CharField(max_length=50, verbose_name="Цвет кожи")
    eye_color = models.CharField(max_length=50, verbose_name="Цвет глаз")
    birth_year = models.CharField(max_length=20, verbose_name="Год рождения")
    gender = models.CharField(max_length=50, verbose_name="Пол")
    
    # ИСПРАВЛЕНИЕ: Мы должны явно указать on_delete. 
    # models.CASCADE - самый простой для объяснения вариант.
    starship = models.ForeignKey(
        Starship,
        on_delete=models.CASCADE, # <--- ЭТОТ ПАРАМЕТР НЕОБХОДИМО ВЕРНУТЬ
        verbose_name="Собственный Корабль",
    )

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"
        ordering = ['name']

    def __str__(self):
        return self.name