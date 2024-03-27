from django.urls import path
from . views import *
app_name = 'recipes'


urlpatterns = [
    path('', home, name="home"),
    path('recipes/<int:id>/', detail, name="recipe"),
    path('recipes/search/', search, name="search"),
    path('recipes/category/<int:category_id>/', category, name="category"),

]