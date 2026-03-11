import requests
import xml.etree.ElementTree as ET


def get_news():
    """
    Fetch top headlines from Google News RSS (free, no API key needed)
    :return: list of dicts with 'title' key, or False on failure
    """
    try:
        url = 'https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en'
        response = requests.get(url, timeout=10)
        root = ET.fromstring(response.content)
        articles = []
        for item in root.findall('.//item'):
            title = item.find('title')
            if title is not None and title.text:
                articles.append({'title': title.text})
        return articles if articles else False
    except Exception as e:
        print(e)
        return False
