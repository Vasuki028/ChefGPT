from preprocess import load_and_clean_data
from recommend import prepare_ingredient_matrix, recommend_recipes

# Step 1: Load and clean the dataset (limit to 1000 for testing)
df = load_and_clean_data()

# Step 2: Print a few rows to confirm it's loaded
print("\n=== First 5 Recipes (cleaned) ===")
print(df.head())

# Step 3: Print details of the first recipe
print("\n=== First Recipe Details ===")
print("Name:", df.iloc[0]['Name'])
print("Calories:", df.iloc[0]['Calories'])
print("Cook Time:", df.iloc[0]['CookTime'])
print("Category:", df.iloc[0]['RecipeCategory'])
print("Ingredients:", df.iloc[0]['ingredients'])
print("Quantities:", df.iloc[0]['quantities'])
print("Instructions:", df.iloc[0]['instructions'])

# Check cleaned images (print only first image URL for brevity)
images = df.iloc[0]['images']
print("Image URL(s):", images if images else "No images found")

# Step 4: Prepare matrix
vectorizer, ingredient_matrix = prepare_ingredient_matrix(df)

# Step 5: Example user input
user_ingredients = ['blueberries', 'sugar', 'lemon']

# Step 6: Recommend recipes
recommendations = recommend_recipes(user_ingredients, df, vectorizer, ingredient_matrix)

# Step 7: Print top matches with key fields
print("\n=== Top Recipe Matches ===")
for index, row in recommendations.head(3).iterrows():
    print(f"\nName: {row['Name']}")
    print("Calories:", row['Calories'])
    print("Cook Time:", row['CookTime'])
    print("Ingredients:", row['ingredients'])
    print("Quantities:", row['quantities'])
    print("Instructions:", row['instructions'][:2], "...")  # Print first 2 steps
    print("Image:", row['images'][0] if row['images'] else "No image")
