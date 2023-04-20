api_key = "851e7a8a45124a60b92459030f1a21f9"

import requests


def get_news(country, api_key=f"{api_key}"):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()

    articles = (content["articles"])
    results = []
    for article in articles:
        results.append(f"TITLE\n'{article['title']}, '\nDescription\n', {article['description']}")
    return results

print(get_news(country="us"))