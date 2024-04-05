from django.urls import reverse, resolve
from recipes import views
from pytest import skip
from .test_recipe_base import RecipeTestBase
# Create your tests here.

class ReceipeCategoryViewTest(RecipeTestBase):

    # category ====================================================================
    def test_recipe_category_view_function_is_ok(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
            )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        # Need a recipe for this test
        titulo = 'This is a category test'
        self.make_recipe(title=titulo)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')
        self.assertIn(titulo, content)

    
    def test_recipe_category_template_dont_load_recipes_not_published(self):
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
             reverse('recipes:category', kwargs={'category_id': recipe.category.id})
            )
        self.assertEqual(response.status_code, 404)

    