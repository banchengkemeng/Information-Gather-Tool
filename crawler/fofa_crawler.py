import json
import tldextract
import re
import yaml
import base64
import requests

def run(search):
    with open("apikey.yaml") as f:
        param = yaml.load(f.read(),Loader=yaml.FullLoader)
        param = param.get('Fofa')
    email = param.get('email')
    key = param.get('key')

    ulist = []
    url = f'https://fofa.info/api/v1/search/all?email={email}&key={key}&qbase64={search}&size=1&fields=host'
    resp = requests.get(url)
    try:
        size = resp.json().get('size')
        if size > 20: size = 20
        url = f'https://fofa.info/api/v1/search/all?email={email}&key={key}&qbase64={search}&size={size}&fields=host'
        resp = requests.get(url)
        ulist.extend(resp.json().get('results'))

        # for u in ulist:
        #     print(f"[+] {u}")
    except:
        print(f"[warning] {resp.json()}")

    uulist = []
    for u in ulist:
        if re.match("http", u) or re.match("https", u):
            u = u.split('/')[2]
        uulist.append(u)
    return uulist

def fofa_domain_run(domain):
    search = f'domain={domain}'
    search = base64.b64encode(search.encode()).decode()
    return run(search)

def fofa_name_run(name):
    search = f'{name}'
    search = base64.b64encode(search.encode()).decode()
    return run(search)

if __name__ == '__main__':
    domain = "auroradss.com"
    fofa_run(domain)