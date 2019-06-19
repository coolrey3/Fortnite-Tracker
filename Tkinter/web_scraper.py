#Import Modules

from bs4 import BeautifulSoup
from tkinter import *
import requests
import webbrowser

#Gui Code
root = Tk()


site ='https://fortnitetracker.com'
apiSite = "https://fortnitetracker.com/api/news-html?cpage="

pageNumber=0
getPage = apiSite + str(pageNumber)
pcPlayer= "/profile/pc/"
xboxplayer = "/profile/pc/"
source = requests.get(getPage).text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())
article = soup.find('article' )
print("Latest Articles")
global news
global eventbox
news = []
eventbox = Listbox(root, height=30, width=150)
eventbox.pack(side ="bottom")
urlList = []

class GUI:

    def __init__(self, master):
        self.master = master
        master.title("Fortnite News")
        master.geometry("500x580")

        self.mainTitle = Label(master, text="Fortnite News and Stat Tracker")
        self.mainTitle.pack()
        self.nameLabel = Label(master, text='Enter player Name: ')
        self.nameLabel.pack(side="top")
        self.playerName = Entry(master, width=50)
        self.playerName.insert(END,'twitch.coolrey3')
        self.playerName.pack(side="top")
        self.playerName.focus()
        self.searchButton = Button(root, text="Search", command=lambda: GUI.search_player(self))
        self.searchButton.pack()

    def search_player(self):
        self.player = self.playerName.get()
        self.playerUrl = site + pcPlayer + self.player
        print(self.playerUrl)
        webbrowser.open(self.playerUrl)




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
        eventbox.insert(END, news)
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
        eventbox.bind("<Double-Button-1>", onDouble)
    except:
        pass


root.bind("<Return>", newsresults)
title = soup.find("h2",class_="trn-article__title")
newsresults("<RETURN>")
my_gui = GUI(root)
root.mainloop()
