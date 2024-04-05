from django.urls import reverse, resolve
from recipes import views
from pytest import skip
from .test_recipe_base import RecipeTestBase
# Create your tests here.

# @skip("Pulando  - test_recipe_detail_view_returns_404_if_no_recipes_found")
class ReceipeSearchViewTest(RecipeTestBase):
    # SEARCH ====================================================================
    def test_recipe_search_loads_right_template(self):
        response = self.client.get(reverse('recipes:search') + "?q=teste")
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        # isso nao passa
        # url = reverse('recipes:search') + "?q=teste"
        # response = self.client.get(url) # 200

        # isso passa
        response = self.client.get(reverse('recipes:search')) 

        self.assertEqual(response.status_code, 404) # 404

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + "?q=<Teste>"
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )