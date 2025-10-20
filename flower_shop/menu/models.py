from django.db import models

# Create your models here.

class MenuFlower(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    description_detail = models.TextField(null=True,blank=True)
    price = models.FloatField()
    discount = models.FloatField()
    image = models.ImageField(null=True,blank=True,upload_to='projects/%Y/%m/%d/')
    category = models.ManyToManyField('FlowerCategory', blank=True)


    # функция которая берет название из сласса и указывает в заголовке в бд
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Каталог цветов"
        verbose_name_plural = "Каталог цветов"



class FlowerCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['-created_at']  # сортировка

class OrderFlower(models.Model):
    flower = models.ForeignKey(MenuFlower, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Заказ от {self.name}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created_at']  # сортировка