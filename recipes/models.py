from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=65)

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)  # adicional uma data na criacao, que nao sera auterada
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/cover/%Y/%m/%d')
    # Category
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # User
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


