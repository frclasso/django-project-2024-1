from django.contrib import admin

# Register your models here.
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeyAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)