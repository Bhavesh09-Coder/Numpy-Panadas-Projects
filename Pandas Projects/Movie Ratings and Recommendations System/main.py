import pandas as pd

# Load the dataset from a CSV file (after downloading it from Kaggle)
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Display the first few rows of the movies and ratings datasets
print("Movies Dataset:")
print(movies.head())
print("\nRatings Dataset:")
print(ratings.head())

# Merge the movies and ratings dataset on 'movieId'
movie_ratings = pd.merge(ratings, movies, on='movieId')

# Analyze movie ratings - Calculate average rating and the number of ratings for each movie
movie_stats = movie_ratings.groupby('title').agg({
    'rating': ['mean', 'count']
}).reset_index()

# Rename columns for easier access
movie_stats.columns = ['title', 'average_rating', 'num_ratings']

# Display top movies by average rating (with at least 100 ratings for quality control)
top_rated_movies = movie_stats[movie_stats['num_ratings'] >= 100].sort_values(by='average_rating', ascending=False)
print("\nTop Rated Movies (at least 100 ratings):")
print(top_rated_movies.head(10))

# Simple Recommendation System - Recommend movies similar to user preferences
def recommend_movies(user_movie):
    """ Recommend movies similar to the given user's preferred movie. """
    user_movie_ratings = movie_ratings[movie_ratings['title'] == user_movie]

    # Find other users who rated the same movie
    users_who_rated = user_movie_ratings['userId'].unique()

    # Find other movies rated by these users
    similar_movies = movie_ratings[movie_ratings['userId'].isin(users_who_rated)]

    # Group by title and calculate average rating and number of ratings for these similar movies
    similar_movie_stats = similar_movies.groupby('title').agg({
        'rating': ['mean', 'count']
    }).reset_index()

    # Rename columns
    similar_movie_stats.columns = ['title', 'average_rating', 'num_ratings']

    # Filter movies with at least 50 ratings
    recommended_movies = similar_movie_stats[similar_movie_stats['num_ratings'] >= 50]

    # Sort movies by average rating
    recommended_movies = recommended_movies.sort_values(by='average_rating', ascending=False)

    return recommended_movies.head(10)

# Example Recommendation for a user who liked 'Toy Story (1995)'
recommended = recommend_movies('Toy Story (1995)')
print("\nRecommended Movies for fans of 'Toy Story (1995)':")
print(recommended)
