import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess

def load_faqs(filename="faqs.json"):
    with open(filename, "r") as file:
        return json.load(file)

def get_best_match(user_question, faqs):
    questions = [faq["question"] for faq in faqs]
    processed_questions = [preprocess(q) for q in questions]
    processed_user = preprocess(user_question)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(processed_questions + [processed_user])
    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    best_index = similarity.argmax()

    return faqs[best_index]["answer"]