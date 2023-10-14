import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed data
data = pd.read_csv('preprocessed_reviews.csv')

# Statistical Summary
mean_rating = data['rating'].mean()
median_rating = data['rating'].median()
std_deviation = data['rating'].std()

print("Statistical Summary:")
print(f"Mean Rating: {mean_rating:.2f}")
print(f"Median Rating: {median_rating}")
print(f"Standard Deviation: {std_deviation:.2f}")

# Data Visualization
# Create a histogram of ratings
plt.figure(figsize=(8, 6))
sns.histplot(data['rating'], kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()
