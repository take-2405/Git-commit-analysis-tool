import os
import requests
from bs4 import BeautifulSoup

date_flag = True

site = requests.get("https://api.github.com/repos/take-2405/Git-commit-analysis-tool/commits")
siteInfo = site.text

path = './result/user.txt'
f = open(path, 'w')

for i in range(0,len(siteInfo)):
    if (siteInfo[i] == "d" and siteInfo[i + 1] == "a" and siteInfo[i + 2] == "t" and siteInfo[i + 3] == "e"):
        if (date_flag):
            f.write(siteInfo[i+7:i+26]+"\n")
            i = i+27
            date_flag = False
        else:
            date_flag = True
    if (siteInfo[i] == "m" and siteInfo[i + 1] == "e" and siteInfo[i + 2] == "s" and siteInfo[i + 3] == "s" and siteInfo[i + 4] == "a" and siteInfo[i + 5] == "g" and siteInfo[i + 6] == "e"):
        f.write(siteInfo[i + 10:i + 16]+"\n")
f.close()
