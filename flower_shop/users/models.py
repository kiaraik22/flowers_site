from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True,max_length=500)
    about_myself = models.TextField(null=True,blank=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='projects/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ['-created']  # сортировка: новые профили первыми

