from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from utils.recipes.factory import make_recipe
from django.db.models import Q
from django.core.paginator import Paginator
from utils.tests.pagination import make_pagination

# Create your views here.

# def home(request):
#     '''Utizando fake data'''
#     return render(request, 'recipes/pages/home.html', context={'recipes': [make_recipe() for _ in range(10)]})
    
def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    page_obj, pagination_range = make_pagination(request, recipes, per_page=9)

    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range
    })





def category(request, category_id):
    recipes = get_list_or_404(
                                Recipe.objects.filter(category__id=category_id, 
                                                      is_published=True).order_by('-id'))

    page_obj, pagination_range = make_pagination(request, recipes, per_page=9)

    return render(request, 'recipes/pages/category.html', context={
                                                                'recipes': page_obj,
                                                                'pagination_range':pagination_range,
                                                                'title':f'{recipes[0].category.name} - Category'
                                                                })

def detail(request, id):
    # recipe =   Recipe.objects.filter(
    #                                     pk=id, 
    #                                     is_published=True).order_by('-id').first()
    
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
                                                                    'recipe': recipe, 
                                                                    'is_detail_page':True,
                                                                    })

def search(request):
    search_term = request.GET.get("q", '').strip()
    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
                                        Q(
                                            Q(title__icontains=search_term) |Q(description__icontains=search_term),
                                            is_published=True
                                        )
                                    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, per_page=9)

    return render(request, 'recipes/pages/search.html',
                  {
                        'page_title': f'Search for "{search_term}" |',
                        'search_term':search_term,
                        'recipes': page_obj,
                        'pagination_range':pagination_range,    
                        'addtional_url_query': f'&q={search_term}',
                  })