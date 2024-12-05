import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import nltk
from flask import Flask, request, render_template
nltk.download('stopwords')
from nltk.corpus import stopwords
import string

# Load dataset
df = pd.read_csv('D:\\Desktop\\dataset.csv')

# Check data distribution
print(df['sentiment'].value_counts())

# Data Preprocessing function
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# Test preprocessing
sample_text = "I love this product, it's amazing!"
print(preprocess_text(sample_text))

df['cleaned_text'] = df['review_text'].apply(preprocess_text)

# Convert text to numerical data using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['cleaned_text'])
y = df['sentiment']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    processed_review = preprocess_text(review)
    review_vector = vectorizer.transform([processed_review])
    prediction = model.predict(review_vector)
    return render_template('result.html', prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
