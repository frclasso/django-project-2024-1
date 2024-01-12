from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from .models import *
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     '''Utizando fake data'''
#     return render(request, 'recipes/pages/home.html', context={'recipes': [make_recipe() for _ in range(10)]})
    
def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={'recipes': recipes})


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')

    if not recipes:
        return HttpResponse(content='Not Found', status=404)

    return render(request, 'recipes/pages/category.html', context={
                                                                'recipes': recipes,
                                                                'title':f'{recipes.first().category.name} - Category'
                                                                })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
                                                                    'recipe': make_recipe(), 
                                                                    'is_detail_page':True,
                                                                    })
