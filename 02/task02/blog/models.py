from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.TextField(unique=True, max_length=100)
    
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.TextField(max_length=200)
    content = models.TextField(default="...")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
