# Movie Ratings and Recommendations System

## Project Overview

This project analyzes movie ratings data and develops a simple recommendation system using Pandas. The dataset used is the **MovieLens 100k Dataset**, which contains movie ratings from users. The system recommends movies based on the average rating and number of ratings for each movie.

## Dataset

The dataset used in this project is the **MovieLens 100k Dataset** provided by GroupLens Research. It contains 100,000 ratings from 943 users on 1,682 movies. The dataset can be downloaded from the following link:

- **[MovieLens 100k Dataset](https://grouplens.org/datasets/movielens/100k/)**
- Direct download link for the dataset: [MovieLens 100k CSV](http://files.grouplens.org/datasets/movielens/ml-100k.zip)

The dataset files used in the project are:
- `u.item`: Contains movie information.
- `u.data`: Contains user ratings for movies.

## Project Structure

The project consists of the following files:

- `main.py`: The Python script that loads the dataset, processes the data, and generates movie recommendations.
- `README.md`: This file containing the project overview and instructions.

## Steps to Run the Project

1. **Download the Dataset**: 
   Download the dataset from [MovieLens 100k Dataset](https://grouplens.org/datasets/movielens/100k/) and extract it.

2. **Install Dependencies**:
   Ensure you have Python installed along with the Pandas library. You can install the required dependencies using the following command:
   ```bash
   pip install pandas
