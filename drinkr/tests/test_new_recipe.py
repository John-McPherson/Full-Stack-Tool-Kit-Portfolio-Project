from django.test import TestCase
from ..new_recipe import recipe_steps, ingredient_list


class TestRecipeSteps(TestCase):
    def test_to_see_function_returns_numbered_array(self):
        self.assertEqual(
            recipe_steps(["step one", "step two", "step three"]),
            ["1. Step one", "2. Step two", "3. Step three"],
        )


class TestIngredientList(TestCase):
    def test_to_see_function_returns_numbered_array(self):
        self.assertEqual(
            ingredient_list(
                ["Rum", "Vodka", "Bitters"],
                ["ml", "ml", "bsp"],
                ["60", "30", "2"],
            ),
            ["60 ml of Rum", "30 ml of Vodka", "2 bsp of Bitters"],
        )
