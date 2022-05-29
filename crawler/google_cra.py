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

    cookie = {
        "HSID":"AigFjMg37JezZAD - Y;",
        "SSID":"AtvTtu6tt5CRCMUtu;",
        "APISID":"t_B3EOLSljkQdpQU / AFCCE0tCLdcUoZ_gb;",
        "SAPISID":"o76LwbzCUsxztNLj / AQ94zVXZ1haHtw1oS;__Secure - 1",
        "PAPISID":"o76LwbzCUsxztNLj / AQ94zVXZ1haHtw1oS;__Secure - 3",
        "SEARCH_SAMESITE":"CgQIrJUB;",
        "SID":"Jwh2OBVPAOKRoLGJDvMChihKF3u2G7GFYmhEPrIVZVQATTPSkSyK0TO9Q - TxE_4ou4Te8g.;__Secure - 1",
        "PSID":"Jwh2OBVPAOKRoLGJDvMChihKF3u2G7GFYmhEPrIVZVQATTPSVGZm033w744Zrn7xkQybLA.;__Secure - 3",
        "P_JAR":"2022 - 05 - 18 - 12;",
        "AEC":"AakniGPPif42bwz09co3tv_Llwd8082Pl2lDjMrbchJsPlJduOiNrWbh1Fg;",
        "NID":"511 = c02YcwtucNVpA5qP8GSraNkyqmRjlAvB3OjSHCHhUTF_KYNGVgT96JChPATbHbiLuhPFN3ieW9BWdlf3qCHtBG5IWrBYODhDuPJVFeZJy - jce9fAk_keY_wI1_XbF7uWcRW2vJvfMy4TWagybQfQpf6hXBZBPtuN3hyoSiCL96VhyyKY6v - mRDEI5Uur85MgKXdHCo8ybSYZ6M1hvaOLmUVFJH - GfA7qlg - R - WCthr_QLt4R68aKITkTzzV6ctWUNNehC5ZByOyP2jQpvImaEwf9AZJbB3Y;",
        "SIDCC":"AJi4QfH_7ZepYAsE0Ei9JilWsgS1Wc1zHvq1AraWhnm - 6GPPktqTfzPmi1lEVvug64nAxZlCYA;__Secure - 3",
        "PSIDCC":"AJi4QfE7uy4EOPbY9Xws7ipj6OWnexnaqKONm5kFw4F7a69aBV4BUtyjOMVoNYopACVKu7p_z7M"
    }
    resp = requests.get(url,headers=header,cookies=cookie)
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
