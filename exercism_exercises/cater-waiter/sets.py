from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    return dish_name, set(dish_ingredients)

def check_drinks(drink_name, drink_ingredients):
    return f"{drink_name} Mocktail" if set(drink_ingredients).isdisjoint(
        set(ALCOHOLS)) else f"{drink_name} Cocktail"

def categorize_dish(dish_name, dish_ingredients):
    categories = [("VEGAN", VEGAN), ("VEGETARIAN", VEGETARIAN), 
                  ("PALEO", PALEO), ("KETO", KETO), ("OMNIVORE", OMNIVORE)]
    
    for category_name, category_ingredients in categories:
        if dish_ingredients.issubset(category_ingredients) == True:
            return f"{dish_name}: {category_name}"
        
def tag_special_ingredients(dish):
    restrictions = set(dish[1]).intersection(SPECIAL_INGREDIENTS)
    return dish[0], restrictions

def compile_ingredients(dishes):
    # bigset = []
    # for each in dishes:
    #     bigset.extend(list(each))
    # return set(bigset)

    return set([ingredient for dish in dishes for ingredient in dish])

def separate_appetizers(dishes, appetizers):
    return list(set(dishes).difference(appetizers))
