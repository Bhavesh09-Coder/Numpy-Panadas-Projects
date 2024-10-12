import numpy as np
import csv

# Initialize lists to hold data
players = []
scores = []
wins = []
losses = []

# Read the CSV file
with open('sports_statistics.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        players.append(row[0])
        scores.append(int(row[1]))
        wins.append(int(row[2]))
        losses.append(int(row[3]))

# Convert lists to NumPy arrays for analysis
scores_array = np.array(scores)
wins_array = np.array(wins)
losses_array = np.array(losses)

# Perform analysis
average_score = np.mean(scores_array)
total_wins = np.sum(wins_array)
total_losses = np.sum(losses_array)
highest_score = np.max(scores_array)
best_player_index = np.argmax(scores_array)

# Output results
print("Sports Statistics Analysis:")
print(f"Average Score: {average_score:.2f}")
print(f"Total Wins: {total_wins}")
print(f"Total Losses: {total_losses}")
print(f"Highest Score: {highest_score} by {players[best_player_index]}")
