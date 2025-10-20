from django.db import models
from django.template.defaultfilters import truncatechars
from users.models import Profile

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='projects/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)

    @property
    def short_content(self):
        return truncatechars(self.content, 100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created']

class Comments(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE,null=True)
    content = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        unique_together = [['owner', 'post']]
        ordering = ['-created']

