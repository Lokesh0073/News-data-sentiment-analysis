import streamlit as st
import requests
from googletrans import Translator
from transformers import pipeline
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Function to fetch news articles
def fetch_news(keyword, api_key, from_date=None, to_date=None):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}"
    if from_date:
        url += f"&from={from_date}"
    if to_date:
        url += f"&to={to_date}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return [
            {
                "title": article["title"],
                "content": article["content"],
                "url": article["url"],
                "publishedAt": article["publishedAt"]
            }
            for article in articles if article["content"]
        ]
    else:
        st.error(f"Failed to fetch news data. Status code: {response.status_code}")
        return []

# Function to translate articles to English
def translate_to_english(articles):
    translator = Translator()
    for article in articles:
        if article["content"]:
            article["content"] = translator.translate(article["content"], dest="en").text
            article["title"] = translator.translate(article["title"], dest="en").text
    return articles

# Function to perform sentiment analysis
def analyze_sentiment(articles):
    sentiment_analyzer = pipeline("sentiment-analysis")
    for article in articles:
        if article["content"]:
            sentiment = sentiment_analyzer(article["content"])[0]
            article["sentiment"] = sentiment
    return articles

# Streamlit App
st.title("News Sentiment Analysis App with Filters")
st.write("Enter a topic to fetch news articles, perform sentiment analysis, and filter results.")

# Input field for topic
topic = st.text_input("Enter topic (e.g., 'Data Science')", "")

# Date filters
st.sidebar.subheader("Filter by Date")
from_date = st.sidebar.date_input("From Date", value=None)
to_date = st.sidebar.date_input("To Date", value=None)

# Sentiment filter
st.sidebar.subheader("Filter by Sentiment")
sentiment_filter = st.sidebar.selectbox("Select Sentiment", ["All", "Positive", "Negative"])

# Button to fetch and analyze
if st.button("Fetch and Analyze"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        
        api_key = API_KEY  
        
        # Convert dates to string format required by NewsAPI
        from_date_str = from_date.strftime('%Y-%m-%d') if from_date else None
        to_date_str = to_date.strftime('%Y-%m-%d') if to_date else None
        
        # Fetch news articles
        st.info("Fetching news articles...")
        news_data = fetch_news(topic, api_key, from_date_str, to_date_str)

        if news_data:
            # Translate articles to English
            st.info("Translating articles to English...")
            translated_news = translate_to_english(news_data)

            # Perform sentiment analysis
            st.info("Analyzing sentiment of articles...")
            news_with_sentiment = analyze_sentiment(translated_news)

            # Filter results based on sentiment
            if sentiment_filter != "All":
                news_with_sentiment = [
                    article for article in news_with_sentiment
                    if article["sentiment"]["label"].lower() == sentiment_filter.lower()
                ]

            # Display results
            if news_with_sentiment:
                st.success("Analysis Complete!")
                for article in news_with_sentiment:
                    st.subheader(article["title"])
                    st.write(f"**Content:** {article['content']}")
                    st.write(f"**URL:** [Read more]({article['url']})")
                    st.write(f"**Published At:** {article['publishedAt']}")
                    st.write(f"**Sentiment:** {article['sentiment']['label']} (Score: {article['sentiment']['score']:.2f})")
                    st.write("---")
            else:
                st.warning("No articles found matching the selected filters.")
        else:
            st.error("No articles found or failed to fetch articles.")
