import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load synthetic Chinese data
input_path = "C:\\MW\\pythonProject\\data_generation\\synthetic_output_chinese\\synthetic_data_chinese.csv"
df = pd.read_csv(input_path, encoding='utf-8')

# Print class distribution to verify
print("Class distribution: ")
print(df['label'].value_counts())

# Create a text column that combines all text fields
df['text'] = df.apply(lambda x: ' '.join(x.drop(['label'], axis=0).astype(str)), axis=1)

# Split into features and target
X = df['text']
y = df['label']

# Vectorize the text data
vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)

# Train the model
model = LogisticRegression()
model.fit(X_vect, y)

# Save the model and vectorizer
output_path = "C:\\MW\\pythonProject\\data_generation\\PKL File\\Chinese pkl\\model_chinese.pkl"
with open(output_path, 'wb') as file:
    pickle.dump((model, vectorizer), file)
print(f"Model and vectorizer saved to {output_path}")
