from django.urls import reverse, resolve
from recipes import views
from pytest import skip
from .test_recipe_base import RecipeTestBase
# Create your tests here.

# @skip("Pulando  - test_recipe_detail_view_returns_404_if_no_recipes_found")
class ReceipeHomeViewTest(RecipeTestBase):
    # home ===============================================================
    def test_recipe_home_view_function_is_ok(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, "recipes/pages/home.html")

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipe(self):
        # Recipe.objects.get(pk=1).delete() ## tem q criar ao menos uma receita
        response = self.client.get(reverse('recipes:home'))
        self.assertIn("Ainda nao temos nenhuma receita publicada, seja o primeiro!", response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
        # Need a recipe for this test
        self.make_recipe()

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_dont_loads_recipes_not_published(self):
        # Need a recipe for this test
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>Ainda nao temos nenhuma receita publicada, seja o primeiro!</h1>',
            response.content.decode('utf-8')
        )
        
    