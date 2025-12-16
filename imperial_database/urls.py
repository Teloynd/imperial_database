# imperial_database/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),

    # Подключаем URL-адреса нашего приложения starwars.
    # Теперь все URL-адреса starwars будут доступны по корневому пути ''
    path('', include('starwars.urls')),
]