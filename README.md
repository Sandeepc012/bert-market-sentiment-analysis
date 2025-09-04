# BERT‑Based Financial Market Sentiment Analysis

This project provides a comprehensive pipeline for analyzing financial market sentiment using transformer‑based models and visualizing the results in real time.  It ingests news articles and social media posts, classifies each text with a fine‑tuned BERT sentiment model, correlates aggregated sentiment with the latest stock price data, and serves the results through a Flask API and interactive D3.js dashboard.

## Features

* **Scalable Data Ingestion** – collects and processes financial news and social media text for sentiment prediction.
* **Transformer Model** – leverages a pre‑trained BERT model for high‑accuracy sentiment classification.
* **Real‑Time Dashboard** – serves a web interface that displays current sentiment distribution and latest stock price using D3.js.
* **Stock Correlation** – fetches live market data using yfinance and correlates it with aggregated sentiment.

## Setup

1. Clone this repository and change into the project directory.
2. Install the Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

   The API will be available at `http://localhost:5000/api/sentiment` and the dashboard at `http://localhost:5000/`.

## Usage

The ingestion and classification pipeline runs each time the API endpoint is called.  The `/api/sentiment` endpoint returns aggregated counts of positive, negative and neutral texts along with the latest SPY price.  The root route (`/`) displays a bar chart of sentiment distribution and a live stock price indicator that refreshes every minute.

## License

This project is released under the MIT License.
