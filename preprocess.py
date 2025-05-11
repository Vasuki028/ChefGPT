import pandas as pd
import re

def parse_r_list(text):
    """
    Converts: c("a", "b", "c") → ['a', 'b', 'c']
    """
    if pd.isna(text):
        return []
    # Use regex to extract quoted strings inside c("...") 
    return re.findall(r'"(.*?)"', text)

def load_and_clean_data(path="data/recipes.csv", limit=5000):
    # Load only required columns
    use_cols = [
        'Name',
        'CookTime',
        'RecipeCategory',
        'Calories',
        'RecipeIngredientParts',
        'RecipeIngredientQuantities',
        'RecipeInstructions',
        'Images',  # Include the Images column here
    ]

    df = pd.read_csv(path, usecols=use_cols, nrows=limit)

    # Drop rows with missing values
    df.dropna(subset=['Name', 'RecipeIngredientParts'], inplace=True)

    # Clean the ingredients
    df['ingredients'] = df['RecipeIngredientParts'].apply(parse_r_list)

    # Clean instructions
    df['instructions'] = df['RecipeInstructions'].apply(parse_r_list)

    # Clean quantities if needed
    df['quantities'] = df['RecipeIngredientQuantities'].apply(parse_r_list)

    # Clean images (parse image URLs from c("..."))
    df['images'] = df['Images'].apply(parse_r_list)

    # You can drop the original columns if not needed
    df = df[['Name', 'Calories', 'CookTime', 'RecipeCategory', 'ingredients', 'quantities', 'instructions', 'images']]

    return df
