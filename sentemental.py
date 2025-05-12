from google.colab import files
import pandas as pd
from textblob import TextBlob

# Load the Excel file directly (Make sure the file is already in the environment)
df = pd.read_excel('anse.xlsx')

# Print column names to verify
print("Available columns:", df.columns)

# Sentiment analysis function
def analyze_sentiment(text):
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis to 'answer' column (adjust if needed)
df['sentiment'] = df['answer'].apply(analyze_sentiment)

# Save to CSV and download
df.to_csv('comments_with_sentiment.csv', index=False)

# Download the file
files.download('comments_with_sentiment.csv')
