from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def predict_sentiments(texts):
    results = sentiment_pipeline(texts)
    sentiments = [r["label"] for r in results]
    scores = [r["score"] for r in results]
    return sentiments, scores
