from bs4 import *
import requests
from PIL import Image
import shutil
import urllib
import os

picList = []

def picURL(code):
    code1 = code.replace('-', '00')

    url = 'https://www2.javhdporn.net/video/'+code
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser').select('body')[0]
    # print(soup.prettify())

    images = []
    for tag in soup.find_all():
        if tag.name == "img":
            images.append(url+tag['src'])

    for i in images:
        i = i.replace('https://www2.javhdporn.net/video/'+code+'https://', '')
        if code1 in i:
            # print(i)
            i = 'https://'+i
            print(i)
            picList.append(i)
            
            filename = code+'.jpg'
            try:
                response = requests.get(i)
                if response.status_code:
                    fp = open(filename, 'wb')
                    fp.write(response.content)
                    fp.close()
                    print('downloaded')
            except:
                print('not downloaded')


f = open("videoNames.txt", "r")
codes = []
content = f.readlines()
for i in range(len(content)):
    a = content[i]
    a = a.replace('\n', '')
    a = a.lower()
    codes.append(a)

os.chdir('./images')
for i in codes:
    picURL(i)