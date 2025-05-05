import sys
import os
import joblib

# Safe load function
def safe_load_model(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    return joblib.load(path)

try:
    # Correct dynamic paths
    model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'fake_news_model.pkl')
    vectorizer_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'vectorizer.pkl')

    model = safe_load_model(model_path)
    vectorizer = safe_load_model(vectorizer_path)

    def predict(text):
        vect_text = vectorizer.transform([text])
        prediction = model.predict(vect_text)
        return "Fake" if prediction[0] == 1 else "Real"

    if __name__ == "__main__":
        if len(sys.argv) < 2:
            raise ValueError("Input text missing! Please provide text to predict.")
        input_text = sys.argv[1]
        result = predict(input_text)
        print(f"Prediction: {result}")

except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(1)
