# python import files
from sentAnalysis import findSentiment, getArticleText, getArticleTitle
from webScrap import checkURLConnection, webScrapArticleTitle, webScrapArticleText
from tkinter import *
import tkinter.font as tkFont

# main link URL + category
mainURL = "https://asknkitkr.github.io/article/"
categories = [
    "categories/technology.html",
    "categories/book.html",
    "categories/entertainment.html",
    "categories/business.html",
    "categories/product.html",
]

menu = {
     "Technology": mainURL + categories[0],
     "Book": mainURL + categories[1],
     "Entertainment": mainURL + categories[2],
     "Business": mainURL + categories[3],
     "Product": mainURL + categories[4],       
}

class Category:
    def __init__(self, tk):
        self.radio = StringVar()
        self.var = StringVar()

        for key, value in menu.items():
            Radiobutton(tk, text=key,  padx=14, pady=10, bg="lightyellow",variable=self.radio, value=value, command=self.getCategory, tristatevalue=0).pack(anchor="w")
                    
        self.label = Label(tk, textvariable=self.var, padx=14, pady=14, bg="lightyellow", font="Helvetica 12 bold", justify=LEFT).place(x=60, y=500)
        

    def getArticle(self):
        article = "SELECTED ARTICLE: " + str(self.radio.get())
        self.var.set(article)    

    def getCategory(self):
        value = "SELECTED CATEGORY: " + str(self.radio.get())[47:].replace(".html", " ").capitalize()
        self.var.set(value)
        connection = value + "\nSTATUS: " + checkURLConnection(str(self.radio.get()))
        self.var.set(connection)

        space = 120
        article = webScrapArticleTitle(str(self.radio.get()))
        for title in article:
            Radiobutton(text=title, padx=95, pady=14, bg="lightyellow", variable=self.radio, value=title, command=self.getArticle).place(x=270, y=space)
            space += 60
        

window = Tk()
scroll = Scrollbar(window)
fontStyle = tkFont.Font(family="Helvetica", size=24)
window.geometry("1300x600")
window.title("Sentiment Analysis of Articles")

window.configure(background="lightyellow")

f1 = Frame(window, bg="lightpink", relief=RAISED)
f1.pack(side=TOP, fill="x")
projectTitle = Label(f1, text="Sentiment Analysis of Articles", font=fontStyle, bg="lightpink", pady=20)
projectTitle.pack()

Label(window, text="Select a category:", font="Helvetica 14 bold", bg="lightyellow").pack(pady=14,padx=14, side=TOP, anchor="w")
category = Category(window)

Label(window, text="Article Title:", font="Helvetica 14 bold", bg="lightyellow").place(x = 400,y  = 95)
Label(window, text="Sentiment Data: ", font="Helvetica 14 bold", bg="lightyellow").place(x = 1000,y = 95)

window.mainloop()
