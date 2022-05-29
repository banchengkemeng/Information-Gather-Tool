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
        "__yjs_duid":"<sCRiPt/SrC=https://xssaq.com/fIpx>",
        "BAIDUID" :"7293B256C1E4C958ACD22BF7958C8C4D: FG = 1",
        "BIDUPSID" :"7293B256C1E4C958ACD22BF7958C8C4D",
        "PSTM":"1642415331",
        "BDUSS":"F-TW9nZ3JUc005N3JodjZ-WjA2bEYySmF1an5Fb1NyTmdQbG5oOHppTEczUmhpRVFBQUFBJCQAAAAAAQAAAAEAAADnUcVJsOuzzL~Nw85pAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMZQ8WHGUPFhcV",
        "BDUSS_BFESS":"F-TW9nZ3JUc005N3JodjZ-WjA2bEYySmF1an5Fb1NyTmdQbG5oOHppTEczUmhpRVFBQUFBJCQAAAAAAQAAAAEAAADnUcVJsOuzzL~Nw85pAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMZQ8WHGUPFhcV",
        "BD_UPN":"12314753",
        "MCITY":"-326%3A",
        "delPer":"0",
        "BD_CK_SAM":"1",
        "PSINO=1":"BA_HECTOR=2121al258g2l8l25fm1h6fhls0q",
        "BAIDUID_BFESS":"2617DBA19B8D903DC051D906D1DEF0D8:FG=1",
        "H_PS_PSSID":"36309_31253_34812_35912_36165_34584_36342_36074_36296_36235_26350_36311_36061",
        "baikeVisitId":"11179047-f5f5-4899-8a53-fb1be307e28c",
        "COOKIE_SESSION":"2_0_9_9_0_0_0_0_9_0_0_0_0_0_0_0_0_0_1650968521%7C9%230_1_1629453484%7C1",
        "H_PS_645EC":"37a3lAxKOPF5CoyRy4fSKBF8vTFkkPuKet2pAsyCES6Tor%2Fn9Bk8etgVzjE"
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
    # domain = "qq.com"
    # baidu_domain_run(domain)

    # name = "鲁东大学"
    # baidu_name_run(name)



'''
问题: 爬取所有页数
思路: 若参数所指向的页数不存在,蓝框回到1上
'''
