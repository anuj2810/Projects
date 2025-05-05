import joblib

model = joblib.load('model/fake_news_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

def predict_news(news_text):
    vect_text = vectorizer.transform([news_text])
    prediction = model.predict(vect_text)
    return prediction[0]

# Test
news = "Breaking: India launches new satellite into orbit."
print("Prediction:", predict_news(news))