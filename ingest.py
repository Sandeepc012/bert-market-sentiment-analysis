import pandas as pd


def fetch_news():
    return [
        {"text": "Stocks rally as earnings beat expectations", "source": "news"},
        {"text": "Federal Reserve signals possible rate cut", "source": "news"},
        {"text": "Tech giants report strong quarterly results", "source": "news"},
    ]


def fetch_tweets():
    return [
        {"text": "Feeling bullish about the market today!", "source": "twitter"},
        {"text": "Market volatility has me worried", "source": "twitter"},
        {"text": "Just bought more shares of my favorite stock", "source": "twitter"},
    ]


def get_combined_data():
    return fetch_news() + fetch_tweets()
