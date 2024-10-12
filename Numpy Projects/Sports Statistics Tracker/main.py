import numpy as np

# Player names and statistics (scores, wins, losses)
players = np.array([
    ['Player', 'Score', 'Wins', 'Losses'],
    ['Alice', 95, 7, 3],
    ['Bob', 87, 6, 4],
    ['Charlie', 92, 8, 2],
    ['David', 78, 5, 5],
    ['Eva', 90, 9, 1]
])

# Extract scores, wins, and losses as numpy arrays
scores = np.array([95, 87, 92, 78, 90])
wins = np.array([7, 6, 8, 5, 9])
losses = np.array([3, 4, 2, 5, 1])

# Functions for analysis
def total_wins(wins_array):
    return np.sum(wins_array)

def total_losses(losses_array):
    return np.sum(losses_array)

def average_score(scores_array):
    return np.mean(scores_array)

def highest_score_player(players_data, scores_array):
    index = np.argmax(scores_array) + 1  # +1 to skip header row
    return players_data[index][0]

def win_loss_ratio(wins_array, losses_array):
    return np.divide(wins_array, losses_array)

# Analysis
print("Total Wins:", total_wins(wins))
print("Total Losses:", total_losses(losses))
print("Average Score:", average_score(scores))
print("Player with Highest Score:", highest_score_player(players, scores))

# Calculate Win/Loss Ratio for each player
ratios = win_loss_ratio(wins, losses)
for i in range(len(players)-1):  # Exclude header row
    print(f"{players[i+1][0]} Win/Loss Ratio: {ratios[i]:.2f}")

# Example: Display Player Statistics
print("\nPlayer Statistics:")
for i in range(1, len(players)):
    print(f"{players[i][0]}: Score={players[i][1]}, Wins={players[i][2]}, Losses={players[i][3]}")
