import streamlit as st
from preprocess import load_and_clean_data
from recommend import prepare_ingredient_matrix, recommend_recipes

# Load and process data
df = load_and_clean_data()
vectorizer, ingredient_matrix = prepare_ingredient_matrix(df)

# Streamlit UI
st.title("🍽️ ChefGPT")

st.markdown("Enter ingredients you have, and we'll recommend recipes!")

# User input
user_input = st.text_input("Enter ingredients (comma separated):", "blueberries, sugar, lemon")

if user_input:
    user_ingredients = [item.strip().lower() for item in user_input.split(',') if item.strip()]
    
    if not user_ingredients:
        st.warning("Please enter at least one ingredient.")
    else:
        # Recommend recipes
        recommendations = recommend_recipes(user_ingredients, df, vectorizer, ingredient_matrix)
        
        if recommendations.empty:
            st.info("No matching recipes found.")
        else:
            st.subheader("🍲 Top Recipe Matches:")

            for idx, row in recommendations.iterrows():
                st.markdown(f"## {row['Name']}")
                
                # Show image if available
                if row['images'] and isinstance(row['images'], list):
                    for url in row['images'][:2]:  # Show only the first 2 images
                        st.image(url, use_container_width=True)
                
                # Show metadata
                st.markdown(f"**Calories:** {row['Calories']}")
                st.markdown(f"**Cook Time:** {row['CookTime']}")
                st.markdown(f"**Category:** {row['RecipeCategory']}")

                # Ingredients + Quantities
                st.markdown("**Ingredients:**")
                if isinstance(row['ingredients'], list) and isinstance(row['quantities'], list):
                    ingredients = row['ingredients']
                    quantities = row['quantities']
                    for i in range(min(len(ingredients), len(quantities))):
                        st.write(f"- {quantities[i]} {ingredients[i]}")
                else:
                    st.write(", ".join(row['ingredients']))

                # Instructions
                st.markdown("**Instructions:**")
                for step in row['instructions']:
                    st.write(f"- {step}")

                st.markdown("---")
