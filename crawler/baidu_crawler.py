# -*- coding: UTF-8 -*-
import re
import requests
import tldextract
from lxml import etree

def black(string):
    try:
        if re.search("gov",string):
            return True
        else:
            return False
    except:
        return False

def run(key,pn):
    url = f"https://www.baidu.com/s?wd={key}&pn={pn-1}*10"
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
    }
    cookie = {
        "BAIDUID" :"C8EFFC521579423691F5BFE5F86D888D:FG=1",
        "BIDUPSID" :"C8EFFC521579423691F5BFE5F86D888D",
        "PSTM":"1661928763",
        "H_PS_PSSID":"36552_36625_36885_36570_36804_36786_37071_37134_26350_37205_37230",
    }
    session = requests.session()
    resp = session.get(url,headers=header,cookies=cookie,timeout=3)
    resp.encoding='utf-8'
    data = etree.HTML(resp.text)
    content_ul = data.xpath("//h3[@class='c-title t t tts-title']/a/@href")
    ulist = []
    for u in content_ul:
        if black(u) == True:
            content_ul.remove(u)
        else:
            uu = u + "&wd="
            resp2 = requests.get(uu)
            rUrl = re.findall(".*URL='(.*)'.*",resp2.text)
            if len(rUrl) != 0:
                if re.match("http",rUrl[0]) or re.match("https",rUrl[0]):
                    u = rUrl[0].split('/')[2]
                ulist.append(u)
    return ulist

def baidu_domain_run(domain):
    ulist = []
    ulist_temp = []
    for i in range (1,20):
        ulist_temp.extend(run(f"site:{domain}",i))

    # 输出
    # for u in ulist_temp:
    #     print(f"[+] {u}")

    ulist.extend(ulist_temp)
    return ulist

def baidu_name_run(name):
    try:
        u = run(name,1)[0]
        u = tldextract.extract(u).registered_domain
        # print(f"[+] {u}")
        return u
    except:
        return "None"

if __name__ == '__main__':
    pass




'''
问题: 爬取所有页数
思路: 若参数所指向的页数不存在,蓝框回到1上
'''
