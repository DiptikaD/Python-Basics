from sets_test_data import *
from sets_categories_data import *
from sets import (
    clean_ingredients, check_drinks, categorize_dish, tag_special_ingredients,
    compile_ingredients, separate_appetizers, singleton_ingredients
)
import unittest

class TestRecipeFunctions(unittest.TestCase):
    
    # Test for de-duplicating recipe ingredients
    def test_clean_ingredients(self):
        test_data = zip(recipes_with_duplicates[::3], recipes_without_duplicates[::3])
        
        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="recipes with duplicated ingredients",
                              result="recipe ingredients de-duped"):

                error_msg = (f"Expected the ingredient list for {item[0]} to be de-duplicated, "
                             "but the ingredients were not cleaned as expected.")

                self.assertEqual(clean_ingredients(item[0], item[1]), (result[1], result[2]), msg=error_msg)

    # Test for classifying drinks correctly
    def test_check_drinks(self):
        test_data = zip(all_drinks[::2], drink_names[::2])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="all drinks", results="drinks classified"):

                error_msg = f"Expected {result} for {item}, but got something else instead."
                self.assertEqual(check_drinks(item[0], item[1]), (result), msg=error_msg)

    # Test for categorizing dishes correctly
    def test_categorize_dish(self):
        test_data = zip(sorted(recipes_without_duplicates, reverse=True)[::3], dishes_categorized[::3])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="all recipes list", results="categorized dishes"):

                error_message = f"Expected category {result} for {item[0]}, but got a different category instead."
                self.assertEqual(categorize_dish(item[1], item[2]), (result), msg=error_message)

    # Test for tagging special ingredients
    def test_tag_special_ingredients(self):
        test_data = zip(dishes_to_special_label[::3], dishes_labeled[::3])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="all recipes list", results="special ingredients tagged"):

                error_message = f"Expected {result} for {item}, but got something else instead."
                self.assertEqual(tag_special_ingredients(item), (result), msg=error_message)

    # Test for compiling all ingredients from all dishes
    def test_compile_ingredients(self):
        test_data = zip(ingredients_only, [VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="all ingredients for all recipes",
                              result="combined list of ingredients for all dishes"):

                error_message = "Expected a proper set of combined ingredients, but something went wrong."
                self.assertEqual(compile_ingredients(item), (result), msg=error_message)

    # Test for separating appetizers
    def test_separate_appetizers(self):
        test_data = zip(dishes_and_appetizers, dishes_cleaned)

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="dishes with appetizers", results="appetizers only"):

                error_message = "Expected only appetizers returned, but some dishes remain in the group."
                result_type_error = f"You returned {type(separate_appetizers(item[0], item[1]))}, but a list was expected."
                self.assertIsInstance(separate_appetizers(item[0], item[1]), list, msg=result_type_error)
                self.assertEqual(sorted(separate_appetizers(item[0], item[1])), (sorted(result)), msg=error_message)

    # Test for identifying singleton ingredients
    def test_singleton_ingredients(self):
        test_data = zip(dishes_and_overlap, singletons)

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="overlapping ingredients", results="ingredients in only one dish"):

                error_message = ("Expected only ingredients that belong to exactly "
                                 "one dish, but got multi-dish ingredients instead.")
                self.assertEqual(singleton_ingredients(item[0], item[1]), (result), msg=error_message)
