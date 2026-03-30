import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
data = pd.read_csv("movies.csv")

# Create similarity matrix
cv = CountVectorizer()
matrix = cv.fit_transform(data['genre'])
similarity = cosine_similarity(matrix)

# Recommendation function
def recommend(movie):
    if movie not in data['title'].values:
        print("Movie not found!")
        return
    
    index = data[data['title'] == movie].index[0]
    distances = list(enumerate(similarity[index]))
    movies_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    print("\nRecommended movies:")
    for i in movies_list:
        print(data.iloc[i[0]].title)

# MAIN PROGRAM (IMPORTANT)
print("Available movies:")
print(data['title'].tolist())

movie_name = input("\nEnter a movie name: ")
recommend(movie_name)

input("\nPress Enter to exit...")   
