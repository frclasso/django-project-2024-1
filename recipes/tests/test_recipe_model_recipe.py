
from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def test_recipe_title_length_is_greater_than_65_chars(self):
        self.recipe.title = "Um valor qualquer" * 5

        with self.assertRaises(ValidationError):
            self.recipe.full_clean() # Faz a validacao e quebra  ValidationError

