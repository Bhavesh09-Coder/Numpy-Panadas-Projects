# Import necessary libraries
import pandas as pd

# Load dataset
movies_url = 'http://files.grouplens.org/datasets/movielens/ml-100k/u.item'
ratings_url = 'http://files.grouplens.org/datasets/movielens/ml-100k/u.data'

# Load movies data
movies_columns = ['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL', 'unknown', 'Action', 'Adventure', 'Animation', 
                  'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance',
                  'Sci-Fi', 'Thriller', 'War', 'Western']
movies_df = pd.read_csv(movies_url, sep='|', names=movies_columns, encoding='latin-1')

# Load ratings data
ratings_columns = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings_df = pd.read_csv(ratings_url, sep='\t', names=ratings_columns)

# Merge both dataframes on 'movie_id'
movie_ratings_df = pd.merge(ratings_df, movies_df[['movie_id', 'title']], on='movie_id')

# Display basic data information
print("Sample data:")
print(movie_ratings_df.head())

# Function to calculate average rating for each movie
average_ratings = movie_ratings_df.groupby('title')['rating'].mean().sort_values(ascending=False)

# Function to calculate number of ratings for each movie
num_ratings = movie_ratings_df.groupby('title')['rating'].count().sort_values(ascending=False)

# Create a DataFrame combining average rating and number of ratings
ratings_summary_df = pd.DataFrame({'average_rating': average_ratings, 'num_ratings': num_ratings})

# Display the top 10 movies by average rating
print("\nTop 10 movies by average rating:")
print(ratings_summary_df.head(10))

# Build a simple recommendation system: Recommend movies based on the highest average rating and number of ratings
def recommend_movies(min_ratings=100):
    """Recommend movies with average rating and number of ratings greater than min_ratings."""
    recommended_movies = ratings_summary_df[ratings_summary_df['num_ratings'] >= min_ratings]
    return recommended_movies.sort_values(by='average_rating', ascending=False).head(10)

# Recommend top 10 movies based on the criteria
print("\nTop 10 recommended movies (min 100 ratings):")
print(recommend_movies(100))
