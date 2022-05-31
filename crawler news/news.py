import io
from traceback import print_tb
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import xml.etree.ElementTree as ET

news_rss = "https://vnexpress.net/rss/tin-moi-nhat.rss"


root = Tk()
root.geometry('350x600')
root.resizable(0,0)
root.title("Breaking news")
#Create label center
label = Label(root, text="Hello") 
label.pack()

#Create picture center
# data_rss = requests.get(news_rss)
# print(data_rss.content())
response = requests.get("https://httpbin.org/xml")

string_xml = response.content
tree = xml.etree.ElementTree.fromstring(string_xml)

print(tree)

img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
raw_data = urlopen(img_url).read()
im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
photo = ImageTk.PhotoImage(im)
picture = Label(root, image=photo)
picture.pack()

root.mainloop()