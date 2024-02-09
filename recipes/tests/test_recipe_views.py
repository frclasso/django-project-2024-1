from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe, User
# Create your tests here.


class ReceipeViewTest(TestCase):

    def setUp(self) -> None:
        category = Category.objects.create(name="Soups")
        author = User.objects.create_user(
            first_name = "John",
            last_name ="Doe",
            username ="johndoe",
            password ="1234565",
            email ="joedoe@email.com"
        )

        recipe = Recipe.objects.create(
                                        category =category,
                                        author=author,
                                        title = "Recipe title",
                                        description = "Recipe description",
                                        slug = "recipe-slug-name",
                                        preparation_time = 10,
                                        preparation_time_unit = "Minutos",
                                        servings = 5,
                                        servings_unit = "Porcoes",
                                        preparation_steps = "Recipe Prepration Steps",
                                        preparation_steps_is_html = False,
                                        is_published = True,
            s
        )
        
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()

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
        Recipe.objects.get(pk=1).delete()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn("Ainda nao temos nenhuma receita publicada, seja o primeiro!", response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn('Recipe title', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porcoes', content)

        response_context_recipes = response.context['recipes']
        self.assertEqual(len(response_context_recipes), 1)

        
        
    # category ====================================================================
    def test_recipe_category_view_function_is_ok(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
            )
        self.assertEqual(response.status_code, 404)

    # detail ====================================================================
    def test_recipe_detail_view_function_is_ok(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.detail)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
            )
        self.assertEqual(response.status_code, 404)
   


