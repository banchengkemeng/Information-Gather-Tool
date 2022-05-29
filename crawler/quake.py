# -*- coding: UTF-8 -*-
import json
import tldextract
import yaml
import re
import requests
url = "https://quake.360.cn/api/v3/search/quake_service"

def run(SearchGrammar):
    with open('apikey.yaml') as file:
        headers = yaml.load(file.read(),Loader=yaml.FullLoader)
        headers = headers.get('360Quake')
    data = {
        "query": f"{SearchGrammar}",
        "start": 0,
        "size": 20,
        "ignore_cache": False,
    }
    ulist = []
    try:
        req = requests.post(url=f"{url}", headers=headers, json=data)
        rsp = json.loads(req.text)
        # print(len(rsp['data']))
        if len(rsp['data']) >=1:
            for assets in rsp["data"]:
                try:
                    u = ""
                    if assets['service']['name'] == 'http/ssl':
                        u = 'https://'+assets['service']['http']['host']
                    elif assets['service']['name'] == 'http':
                        u = 'http://'+assets['service']['http']['host']
                    # print(f"[+] {u}")
                    ulist.extend(u)
                except Exception as e:
                    pass
    except Exception as e:
        try:
            if req.status_code==401:
                    print('[warning] 无效的key')
        except Exception as e2:
            print('[warning] ',e)
    uulist = []
    for u in ulist:
        if re.match("http", u) or re.match("https", u):
            u = u.split('/')[2]
        uulist.append(u)
    return uulist

def quake_domain_run(domain):
    search = f"domain:{domain}"
    return run(search)

def quake_name_run(name):
    search = f"{name}"
    return run(search)

if __name__ == '__main__':
    domain = "auroradss.com"
    quake_run(domain)
