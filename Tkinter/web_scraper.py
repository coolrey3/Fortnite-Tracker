from bs4 import BeautifulSoup
from tkinter import *
import requests
import webbrowser

root = Tk()

class GUI:

    def openarticle(self, event):
        self.webbrowser.open(playerUrl)

    def openarticle(self, event):
        self.webbrowser.open(playerUrl)

    def searchPlayer(self):
        self.player = playerName.get()
        self.playerUrl = site + pcPlayer + player
        self.webbrowser.open(playerUrl)


    def __init__(self, master):
        self.master = master
        master.title("Fortnite News")
        master.geometry("500x580")

        self.mainTitle = Label(master, text="Fortnite News and Stat Tracker")
        self.mainTitle.pack()

        self.playerName = Entry(master, width=50)
        self.playerName.pack(side="top")
        self.nameLabel = Label(master, text='Enter player Name: ')
        self.nameLabel.pack(side="top")

        self.playerName.focus()

        self.searchButton = Button(root, text="Search", command=GUI.searchPlayer)
        self.searchButton.pack()



        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack()
        #
        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

    # def greet(self):
    #     print("Greetings!")










site ='https://fortnitetracker.com'
#https://fortnitetracker.com/api/news-html?cpage=2
apiSite = "https://fortnitetracker.com/api/news-html?cpage="
pageNumber=0
getPage = apiSite + str(pageNumber)


pcPlayer= "/profile/pc/"
source = requests.get(getPage).text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())
article = soup.find('article' )
print("Latest Articles")
global news
global newsbox
news = []
newsbox = Listbox(root, height=30, width=150)
newsbox.pack(side = "bottom")
urlList = []

class Fortnitenews:
    pass


def newsresults(event):
    global url
    global pageNumber
    global getPage
    global source
    global soup
    global onDouble


    for art in soup.find_all('article'):

        time = art.time.text
        headline = art.h2.text
        link = art.h2.a['href']
        url = site + link
        news =  time + " | " + headline
        newsbox.insert(END,news)
        urlList.append(url)


        def onDouble(event):
            widget = event.widget
            selection = widget.curselection()
            index = widget.nearest(event.y)
            i = index
            webbrowser.open(urlList[i])

    print("refreshed news results")
    pageNumber += 1
    getPage = apiSite + str(pageNumber)
    source = requests.get(getPage).text
    soup = BeautifulSoup(source, 'lxml')



    try:
        newsbox.bind("<Double-Button-1>", onDouble)
    except:
        pass








root.bind("<Return>", newsresults)





#print(art.prettify())
title = soup.find("h2",class_="trn-article__title")
newsresults("<RETURN>")



my_gui = GUI(root)
root.mainloop()
