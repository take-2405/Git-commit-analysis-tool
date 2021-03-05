import os
import requests
from bs4 import BeautifulSoup

site = requests.get("https://api.github.com/repos/take-2405/doing_swift/commits")
date_flag = True
# print(site.text)
# data = BeautifulSoup(site.text, "html.parser")
a = site.text

path = './result/user.txt'
f = open(path, 'w')
# print(a)

for i in range(0,len(a)):
    if (a[i]=="d" and a[i+1]=="a" and a[i+2]=="t" and a[i+3]=="e"):
        if (date_flag):
            f.write(a[i+7:i+26]+"\n")
            i = i+27
            date_flag = False
        else:
            date_flag = True
    if (a[i]=="m" and a[i+1]=="e" and a[i+2]=="s" and a[i+3]=="s" and a[i+4]=="a" and a[i+5]=="g" and a[i+6]=="e"):
        f.write(a[i + 10:i + 16]+"\n")
f.close()
# print(data.date)
# print(data.title.text)