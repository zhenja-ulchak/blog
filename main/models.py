from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    description = models.TextField("Опис", null=True, blank=True)
    short_description = models.TextField("Короткий опис", null=True, blank=True)
    date = models.DateTimeField('Дата', default=datetime.now)
    image = models.ImageField("картинка", upload_to='post', null=True)
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
        
    def __str__(self):
        return self.title