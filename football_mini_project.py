import pandas as pd
import matplotlib.pyplot as plt

# Step 1 and 2: Read the dataset
df = pd.read_csv("results.csv")

print("First five rows:")
print(df.head())

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Delete rows with missing values
df = df.dropna()

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Step 3: Exploring the dataset
tuple_count = df.shape[0]
print("\nNumber of tuples in the dataset:", tuple_count)

tournament_count = df["tournament"].nunique()
print("Number of unique tournaments:", tournament_count)

# Step 4: Convert date column to timestamp
df["date"] = pd.to_datetime(df["date"])

matches_2018 = df[df["date"].dt.year == 2018].shape[0]
print("Number of matches played in 2018:", matches_2018)

# Step 5: Home team statistics
home_wins = (df["home_score"] > df["away_score"]).sum()
home_losses = (df["home_score"] < df["away_score"]).sum()
draws = (df["home_score"] == df["away_score"]).sum()

print("\nHome team wins:", home_wins)
print("Home team losses:", home_losses)
print("Draws:", draws)

# Step 6: Pie chart for wins, losses, and draws
results = [home_wins, home_losses, draws]
labels = ["Home Wins", "Home Losses", "Draws"]

plt.figure(figsize=(6, 6))
plt.pie(results, labels=labels, autopct="%1.1f%%")
plt.title("Home Team Results")
plt.show()

# Step 6: Pie chart for neutral column
plt.figure(figsize=(6, 6))
df["neutral"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Neutral Venue Distribution")
plt.ylabel("")
plt.show()

# Unique team names from home_team and away_team
all_teams = pd.concat([df["home_team"], df["away_team"]])
unique_team_count = all_teams.nunique()

print("\nNumber of unique team names:", unique_team_count)
