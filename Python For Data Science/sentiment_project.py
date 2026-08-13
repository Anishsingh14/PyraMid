import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt')

# Initializing NLP tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


# Functions for Data Transformation
def preprocess_text(text):
    """Cleans text: removes punctuation, lowercases, removes stops words, and lemmatizes."""
    # Removing special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I | re.A)
    text = text.lower()
    
    # Tokenization (split into words)
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords and lemmatize
    cleaned_tokens = [
        lemmatizer.lemmatize(word) for word in tokens 
        if word not in stop_words and len(word) > 1
    ]
    
    # Joining tokens back into a string
    return " ".join(cleaned_tokens)

# Loading Data for tranformation and further analysis
data = {
    'review': [
        "The product is absolutely amazing and exceeded my expectations.",
        "It was terrible, broke on the first day, complete waste of money.",
        "Not bad, not great, just average.",
        "Highly recommend this item, great quality for the price.",
        "Very disappointing experience, will not buy again.",
        "The manager was extremely rude and unhelpful, never again.",
        "I love this movie! Best one all year.",
        "It's fine, nothing special, but it works.",
        "Worst delivery service I have ever used, slow and damaged."
    ],
    'sentiment': ['positive', 'negative', 'neutral', 'positive', 'negative', 'negative', 'positive', 'neutral', 'negative']
}
df = pd.DataFrame(data)

# Applying the preprocessing functions
df['cleaned_review'] = df['review'].apply(preprocess_text)
print("Data Preprocessing Demonstration")
print(df[['review', 'cleaned_review']].head())
print("-" * 50)

# Feature Extraction and Training 
X = df['cleaned_review']
y = df['sentiment']
# Split data into training (70%) and testing (30%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initializing and fiting the TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=500)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test) # Transform only for test set

# Initialize and train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

print("--- Training Status ---")
print(f"Features (Unique Terms) Created: {X_train_vec.shape[1]}")
print("Model Training Complete.")



# Model Evaluation
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)

print("--- Model Evaluation Summary ---")
print(f"Overall Accuracy: {accuracy*100:.2f}%")
print("\nClassification Report (Key Metrics):")
print(classification_report(y_test, y_pred))
print("-" * 50)


# Prediction Utility
def predict_sentiment(text):
    # over using the same preprocessor and vectorizer instances
    cleaned = preprocess_text(text)
    vectorized = vectorizer.transform([cleaned])
    return model.predict(vectorized)[0]

test_phrase_1 = "The service was extremely fast and helpful."
test_phrase_2 = "This product broke on the first day, zero stars."

print("--- Live Prediction Test ---")
print(f"Phrase 1: '{test_phrase_1}' -> {predict_sentiment(test_phrase_1).upper()}")
print(f"Phrase 2: '{test_phrase_2}' -> {predict_sentiment(test_phrase_2).upper()}")
print("-" * 50)
