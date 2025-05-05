# ml_model/train_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Load data
fake_df = pd.read_csv("dataset/Fake.csv")
true_df = pd.read_csv("dataset/True.csv")

fake_df["label"] = 0
true_df["label"] = 1

df = pd.concat([fake_df, true_df], axis=0)
df = df[["title", "label"]]

# Vectorize
x = df["title"]
y = df["label"]

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
x_vect = vectorizer.fit_transform(x)

# Train model
model = PassiveAggressiveClassifier()
model.fit(x_vect, y)

# Save model
os.makedirs("backend/model", exist_ok=True)
joblib.dump(model, "backend/model/fake_news_model.pkl")
joblib.dump(vectorizer, "backend/model/vectorizer.pkl")

print("✅ Model training complete.")
