import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download NLTK data (stopwords and wordnet)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Read data from the CSV file with a different encoding (e.g., ISO-8859-1)
data = pd.read_csv('google_reviews.csv', encoding='ISO-8859-1')

# Handle missing values (fill with an empty string)
data['comment'].fillna('', inplace=True)

# Remove outliers or irrelevant information (optional)
# You can apply specific data filtering or cleaning here if needed.

# Text Preprocessing
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Function for text preprocessing
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove punctuation and convert to lowercase
    tokens = [word.lower() for word in tokens if word.isalpha()]
    
    # Remove stop words
    tokens = [word for word in tokens if word not in stop_words]
    
    # Stem or lemmatize (choose one)
    # You can choose between stemming or lemmatization based on your preference
    # Example using stemming:
    # tokens = [stemmer.stem(word) for word in tokens]
    # Example using lemmatization:
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return ' '.join(tokens)

# Apply text preprocessing to the 'comment' column
data['comment'] = data['comment'].apply(preprocess_text)

# Save the preprocessed data to a new CSV file
data.to_csv('preprocessed_reviews.csv', index=False)
