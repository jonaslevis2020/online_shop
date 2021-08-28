

from django.db import models

# Create your models here.

class Category(models.Model):
    """Product category model"""
    category_name = models.CharField(max_length=50, unique=True)
    slug =  models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True, max_length=255)
    category_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.category_name


