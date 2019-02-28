from bs4 import BeautifulSoup
from tkinter import *
import requests
import webbrowser


root = Tk()
root.title("Fortnite News")
root.geometry("500x580")
mainTitle = Label(root, text = "Fortnite News and Stat Tracker")
mainTitle.pack()
playerName = Entry(root,width= 50)
nameLabel = Label(root,text='Enter player Name: ')
nameLabel.pack(side = "top" )
playerName.pack(side = "top")
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
    print("test)")


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
        print(url)
        newsbox.insert(END,news)
        urlList.append(url)


        def onDouble(event):
            widget = event.widget
            selection = widget.curselection()
            index = widget.nearest(event.y)
            value = widget.get(selection[0])
            print(url)
            print(value)
            print(index)
            i = index
            print(urlList)
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

    print(urlList)


def openarticle(event):
    webbrowser.open(playerUrl)

playerName.focus()
#print(time)

def openarticle(event):
    webbrowser.open(playerUrl)

def searchPlayer():
    player = playerName.get()
    print(player)
    playerUrl = site +pcPlayer + player
    print(playerUrl)
    webbrowser.open(playerUrl)




root.bind("<Return>", newsresults)




searchButton = Button(root,text = "Search" ,command = searchPlayer)
searchButton.pack()
print(news)
#print(art.prettify())
title = soup.find("h2",class_="trn-article__title")
newsresults("<RETURN>")

root.mainloop()
