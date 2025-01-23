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