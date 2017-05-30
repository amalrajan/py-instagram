import bs4 as bs
import urllib.request
import sys
import os
from tkinter import *
import tkinter.ttk as ttk


##source = urllib.request.urlopen("https://www.instagram.com/p/BTl6JxolTg3/?taken-by=windows&hl=en")
##
##soup = bs.BeautifulSoup(source, "html5lib")
##
##image_url = soup.find('meta', property="og:image")["content"]
##
##with open("image1.jpg", 'wb') as image:
##    image.write(urllib.request.urlopen(image_url).read())

class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.l_main = Label(text="Instagram Image Downloader", font=("Segoe UI", 18))
        self.l_main.pack()
        self.geometry("300x300")


app = MainWindow()
app.mainloop()
