import joblib
import pickle
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Load the trained model and vectorizer
model = joblib.load("query_classifier.pkl")
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@api_view(["POST"])
def classify_query(request):
    query = request.data.get("query", "")
    if not query:
        return Response({"error": "Query cannot be empty"}, status=400)

    query_tfidf = vectorizer.transform([query])
    prediction = model.predict(query_tfidf)[0]
    category = "Educational" if prediction == 1 else "Non-Educational"

    return Response({"query": query, "category": category})
