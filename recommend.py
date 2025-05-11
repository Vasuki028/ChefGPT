from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def prepare_ingredient_matrix(df):
    # Join ingredient lists into space-separated strings
    df['ingredients_str'] = df['ingredients'].apply(lambda x: ' '.join(x))
    
    # Convert ingredient strings to count vectors (bag of words)
    vectorizer = CountVectorizer()
    ingredient_matrix = vectorizer.fit_transform(df['ingredients_str'])

    return vectorizer, ingredient_matrix

def recommend_recipes(user_ingredients, df, vectorizer, ingredient_matrix, top_n=5):
    # Clean and join user input into a string
    user_ingredients_str = ' '.join([ingredient.lower().strip() for ingredient in user_ingredients])

    # Vectorize user input using the same vectorizer
    user_vector = vectorizer.transform([user_ingredients_str])

    # Compute cosine similarity
    similarity_scores = cosine_similarity(user_vector, ingredient_matrix).flatten()

    # Get top N indices
    top_indices = similarity_scores.argsort()[::-1][:top_n]

    # Return top N recipes
    return df.iloc[top_indices]
