from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    slug = models.CharField('Slug', null=True, max_length=100)
    description = models.TextField("Опис", null=True, blank=True)
    short_description = models.TextField("Короткий опис", null=True, blank=True)
    date = models.DateTimeField('Дата', default=datetime.now)
    image = models.ImageField("картинка", upload_to='post', null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True ,default=None)
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
        
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    title = models.CharField("Заголовок", max_length=255, blank=True)
    slug = models.SlugField(max_length=255,  blank=True ,  null=True, default=None)
    
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return self.title