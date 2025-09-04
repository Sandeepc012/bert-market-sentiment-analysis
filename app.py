from flask import Flask, jsonify, render_template
from ingest import get_combined_data
from model import predict_sentiments
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sentiment')
def sentiment():
    data = get_combined_data()
    texts = [item["text"] for item in data]
    sentiments, scores = predict_sentiments(texts)
    results = []
    for item, sentiment, score in zip(data, sentiments, scores):
        results.append({"text": item["text"], "source": item["source"], "sentiment": sentiment, "score": score})
    positive_count = sum(1 for s in sentiments if s == "POSITIVE")
    negative_count = sum(1 for s in sentiments if s == "NEGATIVE")
    neutral_count = sum(1 for s in sentiments if s not in ("POSITIVE", "NEGATIVE"))
    price_data = yf.Ticker("SPY").history(period="1d")
    latest_price = None
    if not price_data.empty:
        latest_price = price_data["Close"].iloc[-1]
    return jsonify({"results": results, "positive": positive_count, "negative": negative_count, "neutral": neutral_count, "latest_price": latest_price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
