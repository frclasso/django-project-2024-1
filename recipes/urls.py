from django.urls import path
from . views import *

app_name = 'recipes'


urlpatterns = [
    path('', home, name="home"),
    path('recipes/<int:id>/', recipe, name="recipe"),



]