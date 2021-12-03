from bs4 import BeautifulSoup
import requests

from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# To check the connection to the website
def checkURLConnection(url):
    msg = ""
    try:
        urlopen(url)
    except HTTPError as e: # HTTPError is a subclass of URLError
        msg = 'HTTP Error: ' + str(e.code)
    except URLError as e: # URLError is a subclass of OSError
        msg = 'URL Error: ' + str(e.reason)
    else: # No exception was raised
        msg = "Active"
    return msg

# To scrap the article titles from the website
def webScrapArticleTitle(url):
    titles_list = []
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "lxml")
    articles = soup.find_all('div', class_='card')
    for index, article in enumerate(articles):
        title = article.find('div', class_='card-header').text.replace('  ', '').replace('\n', ' ')
        titles_list.append(title)
        # print('{}. {}'.format(index+1, title.replace('\n', ' ')))
    return titles_list

# To scrap the article contents from the website
def webScrapArticleText(url):
    text_list = []
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "lxml")
    articles = soup.find_all('div', class_='card')
    for index, article in enumerate(articles):
        text_articles = article.find('div', class_='card-body').text.replace('  ', '').replace('\n', ' ')
        text_list.append(text_articles)
        # print(text_articles)
    return text_list
