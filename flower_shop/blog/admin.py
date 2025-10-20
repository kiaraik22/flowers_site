from django.contrib import admin
from .models import Posts, Comments

# Register your models here.

from django.contrib import admin
from .models import Posts
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Posts
        fields = '__all__'

class PostsAdmin(admin.ModelAdmin):
    form = PostAdminForm
    # показывает,какие поля будут видны в админке
    list_display = ('title', 'short_content', 'created')

# Как можно сократить описание в админке?

    # делаем выбранные графы кликабельными в админке
    list_display_links = ('title', 'created')

    # добавили поиск по полям
    search_fields = ('title', 'created')

    # добавили фильтр по полям
    list_filter = ('title', 'created')

admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments)