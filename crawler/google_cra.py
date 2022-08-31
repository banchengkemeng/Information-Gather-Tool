# -*- coding: UTF-8 -*-
import requests
import re
import tldextract
from lxml import etree

def run(key,p):
    url = f'https://www.google.com/search?q={key}&start={p}'

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }

    resp = requests.get(url,headers=header)
    data = etree.HTML(resp.text)
    ulist = data.xpath("//div[@class='yuRUbf']/a/@href")
    uulist = []
    for u in ulist:
        if re.match("http", u) or re.match("https", u):
            u = u.split('/')[2]
        uulist.append(u)
    return uulist

def google_run(domain):
    search = f"site:{domain}"
    ulist = []
    for i in range(1,11):
         ulist.extend(run(search,i))
    return ulist

if __name__ == '__main__':
    domain = "auroradss.com"
    google_run(domain)
