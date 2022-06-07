import io
import webbrowser
import requests
import feedparser
import tkinter as tk

from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from urllib.request import urlopen
from PIL import ImageTk,Image

class NewsApp:

    def __init__(self):

        # fetch data
        self.data = self.parse_rss('https://vnexpress.net/rss/suc-khoe.rss')
        # initial GUI load
        self.load_gui()
        # load the 1st news item
        self.load_news_item(0)

    def parse_rss(self, rss_url):
        try: 
            feed = feedparser.parse(rss_url)
            entries = feed.entries
            parsed_info = []
            my_dict = []
        except:
            return None
        else: 
            for item in entries:
                if item:
                    parsed_html = BeautifulSoup(item["summary"], "html.parser")
                    img_src = ""
                    if parsed_html.find("a"):
                        img_src = parsed_html.find("a").find("img").get("src") 
                    
                    parsed_info.append({"title" : item["title"], "link" : item["link"], "description" : parsed_html.text, "img" : img_src})
            return parsed_info

    def retrieve():
        print(ttk.Combo.get())

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.title('Mera News App')
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def callback(self):
        """ get the contents of the Entry and exit
        """
        print("Selected interface: ", self.Combo.get())

    def load_news_item(self,index):

        # clear the screen for the new news item
        self.clear()

        # image
        try:
            # print(self.data[index])
            img_url = self.data[index]['img']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)


        label = Label(self.root,image=photo)
        label.pack()

        # here combobox
        # Combobox creation
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.vlist = ["Option1", "Option2", "Option3",
          "Option4", "Option5"]
 
        self.Combo = ttk.Combobox(self.frame, values = self.vlist)
        self.Combo.set("Pick an Option")
        self.Combo.pack(padx = 5, pady = 5)
        self.Combo.current(0)
        
       
       

        heading = Label(self.root,text=self.data[index]['title'],bg='black',fg='white',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))

        details = Label(self.root, text=self.data[index]['description'], bg='black', fg='white', wraplength=350,justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        
        

        if index != 0:
            prev = Button(frame,text='Prev',width=16,height=3,command=lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=16, height=3,command=lambda :self.open_link(self.data[index]['link']))
        read.pack(side=LEFT)

        # okButton = Button(frame, text='OK',width=16, height=3,command = self.callback)
        # okButton.place(x = 20, y = 60, width=140, height=25)

        if index != len(self.data)-1:
            next = Button(frame, text='Next', width=16, height=3,command=lambda :self.load_news_item(index+1))
            next.pack(side=LEFT)
        
        

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)


obj = NewsApp()
