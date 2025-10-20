from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'created')

    # делаем выбранные графы кликабельными в админке
    list_display_links = ('name', 'username', 'email')

    # добавили поиск по полям
    search_fields = ('name', 'username', 'email')

    # добавили фильтр по полям
    list_filter = ('name', 'username', 'email')


admin.site.register(Profile, ProfileAdmin)
