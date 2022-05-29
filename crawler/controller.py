# -*- coding: UTF-8 -*-
from .tianyancha import *
from .baidu_crawler import *
from .google_cra import *
from .fofa_crawler import *
from .quake import *
import tldextract
import requests
import random
import re


def google_access():
    url = 'https://www.google.com/search'

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }

    cookie = {
        "HSID": "AigFjMg37JezZAD - Y;",
        "SSID": "AtvTtu6tt5CRCMUtu;",
        "APISID": "t_B3EOLSljkQdpQU / AFCCE0tCLdcUoZ_gb;",
        "SAPISID": "o76LwbzCUsxztNLj / AQ94zVXZ1haHtw1oS;__Secure - 1",
        "PAPISID": "o76LwbzCUsxztNLj / AQ94zVXZ1haHtw1oS;__Secure - 3",
        "SEARCH_SAMESITE": "CgQIrJUB;",
        "SID": "Jwh2OBVPAOKRoLGJDvMChihKF3u2G7GFYmhEPrIVZVQATTPSkSyK0TO9Q - TxE_4ou4Te8g.;__Secure - 1",
        "PSID": "Jwh2OBVPAOKRoLGJDvMChihKF3u2G7GFYmhEPrIVZVQATTPSVGZm033w744Zrn7xkQybLA.;__Secure - 3",
        "P_JAR": "2022 - 05 - 18 - 12;",
        "AEC": "AakniGPPif42bwz09co3tv_Llwd8082Pl2lDjMrbchJsPlJduOiNrWbh1Fg;",
        "NID": "511 = c02YcwtucNVpA5qP8GSraNkyqmRjlAvB3OjSHCHhUTF_KYNGVgT96JChPATbHbiLuhPFN3ieW9BWdlf3qCHtBG5IWrBYODhDuPJVFeZJy - jce9fAk_keY_wI1_XbF7uWcRW2vJvfMy4TWagybQfQpf6hXBZBPtuN3hyoSiCL96VhyyKY6v - mRDEI5Uur85MgKXdHCo8ybSYZ6M1hvaOLmUVFJH - GfA7qlg - R - WCthr_QLt4R68aKITkTzzV6ctWUNNehC5ZByOyP2jQpvImaEwf9AZJbB3Y;",
        "SIDCC": "AJi4QfH_7ZepYAsE0Ei9JilWsgS1Wc1zHvq1AraWhnm - 6GPPktqTfzPmi1lEVvug64nAxZlCYA;__Secure - 3",
        "PSIDCC": "AJi4QfE7uy4EOPbY9Xws7ipj6OWnexnaqKONm5kFw4F7a69aBV4BUtyjOMVoNYopACVKu7p_z7M"
    }

    resp = requests.get(url, headers=header, cookies=cookie)
    statu = resp.status_code
    if statu == 200:
        return True
    else:
        return False


def access(url):
    if url == "None":
        return False
    try:
        resp = requests.get(url, timeout=2)
        if resp.status_code == 200:
            return True
        else:
            return False
    except:
        return False


def judge(search):
    keyl = ["公司", "医院", "学院", "大学", "中学", "小学"]
    for key in keyl:
        if re.search(key, search):
            return True
    return False


def crawler_run(search):
    if judge(search) == True:
        url = tianyancha_run(search)
        if access(url) == False:
            url = baidu_name_run(search)
            if url == "None" or url == None:
                return "None"

        domain = tldextract.extract(url).registered_domain
        print(f"[+] 主域名: {domain}")
        ul = []
        ul.extend(baidu_domain_run(domain))
        if google_access() == True: ul.extend(google_run(domain))
        ul.extend(fofa_domain_run(domain))
        ul.extend(quake_domain_run(domain))
    else:
        ul = []
        ul.extend(fofa_name_run(search))
        ul.extend(quake_name_run(search))

    if len(ul) == 0:
        return "None"
    else:
        return ul
