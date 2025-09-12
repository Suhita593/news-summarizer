import requests

API_KEY = "68991a315396438799fc36158a740d36"
BASE_URL = "https://newsapi.org/v2/everything"

def fetch_news(query, max_articles=3):
    params = {
        "q": query,
        "apiKey": API_KEY,
        "language" : "en",
        "pageSize":max_articles
    }

    response = requests.get(BASE_URL, params = params)

    if response.status_code == 200:
        data = response.json()
        articles = [article["content"] for article in data["articles"] if article["content"]]
        return articles
    
    else:
        print(f"Error fetching news:", response.status_code)
        return []