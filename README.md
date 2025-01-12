# News Sentiment Analysis App with Filters

This is a Streamlit-based web application that fetches news articles using the NewsAPI, translates them to English (if needed), performs sentiment analysis using a Hugging Face model, and allows users to filter the results based on date and sentiment.

## Features

- Fetch news articles based on a topic using the [NewsAPI](https://newsapi.org/).
- Translate articles to English using the Google Translate API.
- Perform sentiment analysis using a pre-trained Hugging Face model.
- Filter articles by date and sentiment (Positive, Negative, All).
- View detailed results with titles, content, publication date, sentiment labels, and links to full articles.

## Installation

### Prerequisites
- Python 3.8 or later
- A NewsAPI API key (sign up [here](https://newsapi.org/register) to get your API key).

### Setup

1. Clone this repository:
      ```bash
      git clone https://github.com/your-username/news-sentiment-analysis.git
      cd news-sentiment-analysis


2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate # For Linux/MacOS
   venv\Scripts\activate    # For Windows

4. Install the required packages:
   pip install -r requirements.txt

5. Create a .env file in the root directory and add your API key:
   API_KEY=your_newsapi_key


Run the App
Start the Streamlit app:
   streamlit run news_data_sentiment_analysis_filter.py


Using the App
Enter a topic in the input box (e.g., "HMVP Virus").
Use the sidebar to filter articles by date or sentiment.
Click "Fetch and Analyze" to view results.

Technologies Used
Streamlit: For building the web interface.
NewsAPI: For fetching news articles.
Googletrans: For translating articles to English.
Hugging Face Transformers: For sentiment analysis.
Python dotenv: For managing API keys securely.

Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.


Contact
For questions or feedback, contact:

Email: lsarode2000@gmail.com.com
GitHub: Lokesh0073
