from django.db import models

# Create your models here. LOS MODELOS SERAN TABLAS EN LA BASE DE DATOS

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank = True)

    def __str__(self):
        return self.title
