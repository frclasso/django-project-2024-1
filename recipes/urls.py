from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name="home"),
    path('recipes/<int:id>/', recipe, name="recipe"),



]