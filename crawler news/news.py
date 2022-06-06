import io
from traceback import print_tb
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
import feedparser
MAX_LINKS = 5


corpus_file = open('corpus.txt', mode='a', encoding='utf8')

rss_re = re.compile(r'/rss/[a-z-?]+.rss', flags=re.UNICODE)
word_re = re.compile('(\w+)', flags=re.UNICODE)  # Chưa chính xác.

parsed_rss = []
parsed_links = []

stop = False


main_url = 'https://vnexpress.net'
main_soup = BeautifulSoup(requests.get(main_url + '/rss').content)
session = requests.Session()
for a in main_soup.find_all('a'):
    if 'href' in a.attrs and rss_re.match(a['href']):
        rss_link = main_url + a['href']

        if rss_link not in parsed_rss:
            print('Parsing RSS: ' + rss_link)
            feed = feedparser.parse(rss_link)
            items = feed.entries
            for item in items:
                try:
                    title = item.title
                    summary = item.summary
                    links = item.links[0]['href']
                    root = Tk()
                    root.geometry('350x600')
                    root.resizable(0,0)
                    root.title("Breaking news")
                    #Create label center
                    label = Label(root, text=title) 
                    label.pack()

                    #Create picture center
                    img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
                    raw_data = urlopen(img_url).read()
                    im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
                    photo = ImageTk.PhotoImage(im)
                    picture = Label(root, image=photo)
                    picture.pack()

                    root.mainloop()
                    #print(links)
                except:
                    print('Error, skipping...')

                

            
        if stop:
            break

# news_rss = "https://vnexpress.net/rss/tin-moi-nhat.rss"


# root = Tk()
# root.geometry('350x600')
# root.resizable(0,0)
# root.title("Breaking news")
# #Create label center
# label = Label(root, text="Hello") 
# label.pack()

# #Create picture center
# # data_rss = requests.get(news_rss)
# # print(data_rss.content())
# response = requests.get("https://httpbin.org/xml")

# string_xml = response.content
# tree = xml.etree.ElementTree.fromstring(string_xml)

# print(tree)

# img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
# raw_data = urlopen(img_url).read()
# im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
# photo = ImageTk.PhotoImage(im)
# picture = Label(root, image=photo)
# picture.pack()

# root.mainloop()