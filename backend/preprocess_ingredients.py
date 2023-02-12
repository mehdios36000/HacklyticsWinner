import pandas as pd
from pandas import DataFrame
from tqdm import tqdm

if __name__ == "__main__":
    recipe_df = pd.read_csv("./data/IngredientsAndRecipe.csv")
    ingredient_df = pd.read_csv("./data/ingr_to_food.csv")

    target_ingredients = list(ingredient_df["Ingredient"])

    recipe_df["Ingredients"] = recipe_df["Cleaned_Ingredients"].map(
        lambda value: (" ".join(eval(value))).lower()
    )

    del recipe_df["Cleaned_Ingredients"]

    has_ingredients = {}
    for ingredient in tqdm(target_ingredients):
        ingredient = ingredient.lower()
        has_ingredients[ingredient] = recipe_df["Ingredients"].map(
            lambda ing: ingredient in ing
        )
    recipe_with_ingredients = recipe_df.to_dict()
    recipe_with_ingredients.update(has_ingredients)

    df = pd.DataFrame(recipe_with_ingredients)
    df.to_csv("./data/cleaned-recipe.csv", index=False)
