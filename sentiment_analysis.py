from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

# Load the CSV data
data = pd.read_csv('preprocessed_reviews.csv')

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define a function to classify sentiment
def classify_sentiment(text):
    # Check for NaN or missing values
    if pd.isna(text) or text == '':
        return 'neutral'
    
    sentiment = analyzer.polarity_scores(text)
    compound_score = sentiment['compound']
    
    if compound_score >= 0.05:
        return 'positive'
    elif compound_score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Add a 'sentiment' column to the DataFrame
data['sentiment'] = data['comment'].apply(classify_sentiment)

# Save the DataFrame with the sentiment labels
data.to_csv('data_with_sentiment.csv', index=False)
