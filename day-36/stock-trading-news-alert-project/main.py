import requests
from twilio.rest import Client

# constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "your-Alpha-Vantage-API-Key"  # set your stock Alpha Vantage API Key

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "your-news-API-Key"  # set your news API Key

TWILIO_SID = "your-Twilio-SID-here"  # set your Twilio SID here
TWILIO_TOKEN = "your-Twilio-auth-Token-here"  # set your Twilio auth Token here

# stock Alpha Vantage parameters
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()
# print(stock_data)

close_price = [float(day["4. close"]) for day in stock_data.values()]

yesterday_price = close_price[0]
previous_price = close_price[1]  # day before yesterday

rate = abs((yesterday_price - previous_price) / yesterday_price) * 100  # percentage

# if increase or decrease 4% or more, get 3 articles and send 3 separated sms messages
if rate >= 4:
    print("Get News")

    # News API parameters
    news_parameters = {
        "q": COMPANY_NAME,
        "apikey": NEWS_API_KEY,
        "searchIn": "title",
        "sortBy": "relevancy"
    }

    # get the first 3 news articles
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_data = news_response.json()["articles"][:3]

    # list with 3 first more relevance articles
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news_data]

    # initiate Twilio Client to send sms message
    client = Client(TWILIO_SID, TWILIO_TOKEN)

    # send 3 separated messages
    for article in formatted_articles:
        message = client.messages \
            .create(
                 body=article,
                 from_="your-active-number-here",  # set your active number here
                 to="your-verified-number-here"  # set your verified number here
             )
        print(message.status)
