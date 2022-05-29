# -*- coding: UTF-8 -*-
import re
import requests
from lxml import etree

def access(url):
    try:
        resp = requests.get(url,timeout=3)
        sc = resp.status_code
        if sc == 200 or sc == 301 or sc == 403:
            data = etree.HTML(resp.text)
            charset = re.findall(".*<meta.*?charset=(.*?)\".*",resp.text)[0]
            if charset == "":
                charset = data.xpath("//meta/@charset")[0]
            resp.encoding = charset
            title = re.findall(".*?<title>(.*)</title>.*?",resp.text)[0]
            return title
        else:
            return None
    except:
        return None

def run(ulist):
    ulist = uniq(ulist)
    u_t = {}
    for u in ulist:
        if re.match("http",u):
            title = access(u)
            if u not in u_t.keys() and title != None:
                u_t[u] = title
                print(f"[+] URL:{u} | TITLE:{u_t[u]}")
        else:
            u1 = 'https://' + u
            title = access(u1)
            if title != None:
                if u1 not in u_t.keys():
                    u_t[u1] = title
                    print(f"[+] URL:{u1} | TITLE:{u_t[u1]}")
            else:
                u2 = 'http://' + u
                title = access(u2)
                if u2 not in u_t.keys() and title != None:
                    u_t[u2] = title
                    print(f"[+] URL:{u2} | TITLE:{u_t[u2]}")
    return u_t

def uniq(ulist):
    ulist = list(set(ulist))
    return ulist

def assethandle_run(ulist):
    u_t = run(ulist)
    return u_t

if __name__ == '__main__':
    ul = [
        "www.dedecms.com/",
        "www.dedecms51.com/dedejiaocheng/guzha/147261.html",
        "baijiahao.baidu.com/s?id=1717932378114857510&wfr=spider&for=pc",
        "baijiahao.baidu.com/s?id=1712022964392338033&wfr=spider&for=pc",
        "http://www.dede888.com/",
        "https://www.chinaz.com/tags/Dede.shtml",
        "https://www.dedesos.com/",
        "http://www.dedeyuan.com/xueyuan/dedejc/7482.html",
        "https://www.dede58.com/a/dedebq/2018/0613/8074.html",
        "www.cssmoban.com/tags.asp?n=dede%E6%A8%A1%E6%9D%BF",
        "baijiahao.baidu.com/s?id=1688918676939631986&wfr=spider&for=pc",
        "www.dedehome.com/",
        "t.zoukankan.com/jijm123-p-10321173.html",
        "www.zhihu.com/people/huang-zhong-zhan",
        "www.dedecms51.com/tags/dede.html",
        "www.dede58.com/",
        "www.imdb.com/title/tt5638952/",
        "www.dedecmsmb.com/",
        "www.360doc.com/content/11/0310/20/177226_100000174.shtml",
        "www.chinatianyin.com/productny/typeid/31/id/87.html",
        "www.dedemao.com/dedemuban/",
    ]

    assethandle_run(ul)

