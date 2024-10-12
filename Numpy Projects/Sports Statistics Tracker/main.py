import numpy as np

# Define a function to save the statistics to a CSV file
def save_to_csv(filename, players, scores, records):
    with open(filename, 'w') as f:
        f.write("Player Name,Score,Win/Loss\n")
        for i in range(len(players)):
            f.write(f"{players[i]},{scores[i]},{records[i]}\n")

# Initialize player data
players = np.array([
    "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", 
    "Ian", "Jack", "Karen", "Liam", "Mia", "Noah", "Olivia", "Paul", 
    "Quinn", "Rita", "Sam", "Tina", "Uma", "Vera", "Will", "Xena", 
    "Yara", "Zane", "Amy", "Ben", "Cara", "Derek", "Ella", "Felix", 
    "Gina", "Hugo", "Ivy", "Jade", "Kirk", "Lola", "Milo", "Nina", 
    "Oscar", "Pia", "Quincy", "Ray", "Sophie", "Tom", "Ulysses", 
    "Violet", "Wendy", "Xander", "Yvonne", "Zach", "Alex", "Brittany", 
    "Carlos", "Diana", "Eric", "Fiona", "George", "Holly", "Iris", 
    "Jake", "Kelsey", "Leo", "Monica", "Nolan", "Opal", "Pauline", 
    "Quinton", "Riley", "Sandra", "Tyler", "Ursula", "Victor", "Wendy", 
    "Xander", "Yasmine", "Zane", "Abby", "Brad", "Clara", "Derek", 
    "Elena", "Frankie", "Ginger", "Hank", "Ivy", "Jasper", "Kimberly", 
    "Liam", "Mia", "Nathan", "Olivia"
])

scores = np.random.randint(0, 100, size=len(players))
records = np.random.choice(["Win", "Loss"], size=len(players))

# Calculate statistics
average_score = np.mean(scores)
win_count = np.sum(records == "Win")
loss_count = np.sum(records == "Loss")

# Print statistics
print(f"Average Score: {average_score:.2f}")
print(f"Total Wins: {win_count}")
print(f"Total Losses: {loss_count}")

# Save statistics to CSV
save_to_csv("sports_statistics.csv", players, scores, records)
print("Statistics saved to sports_statistics.csv")
