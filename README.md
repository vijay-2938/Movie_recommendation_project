# Movie_recommendation_project
_________________________________________________________________________________________________________________________________________________________________________________________________

NAME: K.VIJAYARAJANATHAN

REG NO: 25BAS10053
________________________________________________________________________________________________________________________________________________________________________________________________

# Movie Recommendation System

This project implements a simple content-based movie recommendation system using Python and basic machine learning techniques. The system suggests movies based on similarity in genres.

# Overview

The recommendation system takes a movie title as input and returns a list of similar movies. It uses text vectorization and cosine similarity to identify relationships between movies based on their genres.

# Features
  Content-based recommendation approach ,
  Uses cosine similarity for matching ,
  Simple and easy to understand implementation ,
  Works offline with a small dataset ,

# Technologies Used
  Python ,
  Pandas ,
  Scikit-learn ,


# How It Works
The dataset is loaded using pandas .
The genre column is converted into numerical vectors using CountVectorizer.
Cosine similarity is calculated between all movies.
When a user enters a movie name, the system finds and displays the most similar movies.

How to Run the Project
  Make sure Python is installed on your system.
  
 1 .     Install required libraries:
  
 2  .    pip install pandas scikit-learn
  
 3   .   Run the program:
  
 4    .  python main.py
  
 5     . Enter a movie name when prompted.
  
# Example


# Input:

Inception

# Output:

# Recommended movies:
Interstellar ,
Conjuring ,
Insidious ,

# Limitations
   Uses a small dataset ,
   Recommendations are based only on genre ,
   Does not include user preferences or ratings ,
  
# Future Improvements
   Use a larger dataset (e.g., IMDb or TMDB) ,
   Include movie descriptions for better accuracy ,
   Add a graphical user interface ,
   Deploy as a web application ,
