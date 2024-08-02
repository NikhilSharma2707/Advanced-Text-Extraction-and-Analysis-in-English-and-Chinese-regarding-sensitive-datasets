import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Load the model and vectorizer
with open('path_to_your_model.pkl', 'rb') as file:
    model, vectorizer = pickle.load(file)


def predict_sensitive(text):
    # Vectorize the input text
    X_new = vectorizer.transform([text])

    # Make prediction
    prediction = model.predict(X_new)

    return prediction[0]


# Example usage
text = "Example text with sensitive information."
prediction = predict_sensitive(text)
print(f"Prediction: {prediction}")
