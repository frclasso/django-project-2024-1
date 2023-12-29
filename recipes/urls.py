from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name="home"),
    path('sobre/', sobre, name="sobre"),
    path('contato/', contato, name="contato"),


]