# python import files
from sentAnalysis import passSentimentList
from webScrap import checkURLConnection, webScrapArticleTitle, webScrapArticleText
from colorama import *
from prettytable import PrettyTable
import pyfiglet



# main link URL + category
mainURL = "https://asknkitkr.github.io/article/"
categories = [
    "categories/technology.html",
    "categories/book.html",
    "categories/entertainment.html",
    "categories/business.html",
    "categories/product.html",
]

MENU = {
     1: "Technology",
     2: "Book",
     3: "Entertainment",
     4: "Business",
     5: "Product",       
}

init()

def menu():
    Menu = PrettyTable(["CHOICE", "OPTIONS"])
    Menu.add_row(["S", "Show Category"])
    Menu.add_row(["A", "About Us"])
    Menu.add_row(["E", "Exit"])
    print(Menu)
    choice = input(Fore.LIGHTGREEN_EX + "Enter Choice: ")
    if choice == "S" or choice == "s":
        showCategory()
    elif choice == "A" or choice == "a":
        aboutUs()
    elif choice == "E" or choice == "e":
        exit()
    else:
        print(Fore.RED + "Invalid Choice")
        Menu()

def aboutUs():
    print(Fore.YELLOW)
    about = PrettyTable(["UID","NAME", "WORK"])
    about.add_row(["19BCS1559", "Tushar Lohani", "Sentiment Analysis, Research"])
    about.add_row(["19BCS1561", "Ankit Kumar", "Web Scrapping, Sentiment Analysis"])
    about.add_row(["19BCS1570", "Sakshi Kumari", "Research, Documentation, Testing"])
    print(about)
    while(True):
        op = input("Press B to back: ")
        if op == 'B' or op == 'b':
            menu()
        else:
            print(Fore.RED + "Invalid Input")

def showCategory():
    print(Fore.YELLOW + "\nSELECT CATEGORY:")
    category = PrettyTable(["CHOICE", "OPTIONS"])
    for key, value in MENU.items():
        category.add_row([key , value])
    print(category)
    i=1
    choice = input(Fore.LIGHTGREEN_EX + "Enter Choice: ")
    getArticle(int(choice))

    
def getArticle(n):
    i = 1
    if(checkURLConnection(mainURL + categories[n-1])):
        print(Fore.GREEN + "\nSTATUS: CONNECTED\n")
    else:
        print(Fore.RED + "\nSTATUS: NOT CONNECTED\n")

    url = mainURL + categories[n-1]
    article_title = getArticles(url)
    for title in article_title:
        print(Fore.LIGHTCYAN_EX + str(i) + ". " + title)
        i += 1 
    select_article = int(input(Fore.LIGHTGREEN_EX + "Enter Article Number: "))
    if select_article == 1:
        print(Fore.LIGHTWHITE_EX + webScrapArticleText(url)[0])
        print(Fore.LIGHTYELLOW_EX + "\nSentiment of the Article: " + str(passSentimentList(url)[0]))     
    elif select_article == 2:
        print(Fore.LIGHTWHITE_EX + webScrapArticleText(url)[1])
        print(Fore.LIGHTYELLOW_EX + "\nSentiment of the Article: " + str(passSentimentList(url)[1]))
    elif select_article == 3:
        print(Fore.LIGHTWHITE_EX + webScrapArticleText(url)[2])
        print(Fore.LIGHTYELLOW_EX + "\nSentiment of the Article: " + str(passSentimentList(url)[2]))
    elif select_article == 4:
        print(Fore.LIGHTWHITE_EX + webScrapArticleText(url)[3])
        print(Fore.LIGHTYELLOW_EX + "\nSentiment of the Article: " + str(passSentimentList(url)[3]))
    elif select_article == 5:
        print(Fore.LIGHTWHITE_EX + webScrapArticleText(url)[4])
        print(Fore.LIGHTYELLOW_EX + "\nSentiment of the Article: " + str(passSentimentList(url)[4]))

def articleText(n):
    url = mainURL + categories[n-1]
    article_text = getArticleContent(url)
    for n in article_text:
        print(article_text[n])

def getArticles(url):
    article_title = webScrapArticleTitle(url)
    return article_title

def getArticleContent(url):
    article_text = webScrapArticleText(url)
    return article_text

result = pyfiglet.figlet_format("Sentiment Analysis of articles")
print(result)
#print(Fore.CYAN + "████ SENTIMENT ANALYSIS OF ARTICLES ████")
print(Fore.CYAN + "==================================================================================================================================")
menu()