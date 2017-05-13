import os
import urllib2 as ulib
from bs4 import BeautifulSoup as bs
import requests

#chapter = 5

#my_dir = "/home/pun/OnePiece/"+str(chapter)+"/"
my_dir = raw_input("Enter the directory you want to store:")
if(my_dir==""):
	my_dir="/home/pun/"	
if os.path.isdir(my_dir)==False:
    os.makedirs(my_dir)



#link = "http://www.mangapanda.com/one-piece/"+str(chapter)+"/"
link = raw_input("Enter the link of the first chapter of the comic:");
i=1;
while(1):
    try:
        my_link = link + str(i)
        page = ulib.urlopen(my_link)
        formatted_page = bs(page,"lxml")
        img_holder = formatted_page.find(id="img")

        img_link = img_holder.get("src")

        save_dir = my_dir + str(i) +".jpg"
        print img_link;
        f = open(save_dir,"wb")
        f.write(requests.get(img_link).content)
        i=i+1
        f.close()
    except:
        print link + str(i)
        break;
