import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np
import pickle

# Load the dataset
df = pd.read_csv('C:/MW/pythonProject/data_generation/synthetic_output/synthetic_data.csv')

# Convert all columns to string to avoid concatenation issues
df = df.astype(str)

# Combine text columns into a single feature
X = df['Full Name'] + ' ' + df['Date of Birth'] + ' ' + df['Social Security Number'] + ' ' + \
    df['Address'] + ' ' + df['Phone Number'] + ' ' + df['Email Address'] + ' ' + \
    df['Bank Name'] + ' ' + df['Account Number'] + ' ' + df['Routing Number'] + ' ' + \
    df['Credit Card Number'] + ' ' + df['Expiration Date'] + ' ' + df['CVV']

# Simulate a more realistic target variable with random binary classes
np.random.seed(42)  # For reproducibility
df['IsSensitive'] = np.random.choice([0, 1], size=len(df))
y = df['IsSensitive']

# Vectorize the text data
vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Confusion Matrix:')
print(conf_matrix)
print('Classification Report:')
print(class_report)

# Save the model and vectorizer
with open(r'C:\MW\pythonProject\data_generation\PKL File\model.pkl', 'wb') as file:
    pickle.dump((model, vectorizer), file)