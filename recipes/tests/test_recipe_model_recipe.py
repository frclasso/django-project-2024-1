
from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def make_recipce_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name='Default Category test'),
            author=self.make_author(username='New User'),
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug-1',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps'
        )
        recipe.full_clean()
        recipe.save()
        return recipe
    # def test_recipe_title_length_is_greater_than_65_chars(self):
    #     self.recipe.title = "Um valor qualquer" * 5

    #     with self.assertRaises(ValidationError):
    #         self.recipe.full_clean() # Faz a validacao e quebra  ValidationError

    @parameterized.expand([('title', 65),('description', 165),('preparation_time_unit', 65),('servings_unit', 65)])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1)) # selecar 0, ou seja, nao alterar o length, falha
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        '''Alterando no model pra True, falhas'''
        recipe = self.make_recipce_no_defaults()
        self.assertFalse(recipe.preparation_steps_is_html,
                        msg='Recipe preparation_steps_is_html is True by default.') 
        
    def test_recipe_is_published_by_default(self):
        '''Alterando no model pra True, falhas'''
        recipe = self.make_recipce_no_defaults()
        self.assertFalse(recipe.is_published,
                        msg='Recipe is_published is True by default.')
        
    def test_recipe_model_string_representation(self):
        self.recipe.title = 'Testing representation!'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe), 
            'Testing representation!',
            msg=f'Recipe string representation must be equals {self.recipe.title}'
            )