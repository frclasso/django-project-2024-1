from django.test import TestCase
from django.urls import reverse

class ReceipeURLTest(TestCase):

    def test_pytest_is_ok(self):
        assert 1 == 1

    def test_recipe_home_url_is_ok(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_ok(self):
        # url = reverse('recipes:category', args=(1,))
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_ok(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')
