from textblob import TextBlob
from webScrap import webScrapArticleText

mainURL = "https://asknkitkr.github.io/article/"
categories = [
    "categories/technology.html",
    "categories/book.html",
    "categories/entertainment.html",
    "categories/business.html",
    "categories/product.html",
]

def findSentiment(val):
    if val <= 0.1 and val >= -0.1:
        return "Neutral"
    elif val > 0.1:
        return "Positive"
    else:
        return "Negative"

# def getArticleTitle(url):
#     for i in range(len(webScrapArticleTitle(url))):
#       #  print(webScrapArticleTitle(url)[i])
#         data = webScrapArticleTitle(url)[i]
#         blob = TextBlob(data)
#         sentiment = findSentiment(blob.sentiment.polarity)
#         print(sentiment + ": " + str(blob.sentiment.polarity))

# def getArticleText(url):
#     for i in range(len(webScrapArticleText(url))):
#        # print(webScrapArticleText(url)[i])
#         data = webScrapArticleText(url)[i]
#         blob = TextBlob(data)
#         sentiment = findSentiment(blob.sentiment.polarity)
#         return sentiment
#         # print(sentiment + ": " + str(blob.sentiment.polarity))

def passSentimentList(url):
    sentiment = []
    for i in range(len(webScrapArticleText(url))):
        data = webScrapArticleText(url)[i]
        blob = TextBlob(data)
        sentiment.append(findSentiment(blob.sentiment.polarity))
        # polarity.append(blob.sentiment.polarity)
    return sentiment

