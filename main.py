# -*- coding: UTF-8 -*-
from assethandle.assethandle import assethandle_run
from cdnident.cdnChinaz import cdnChinaz
from cdnident.cdnFinder import cdnFinder
from wafw00f.wafident import *
from fingeridnet.run import finger_run
from pathscan.dirsearch import dirscan_run
from portscan.portscan import portscan_run
from crawler.controller import crawler_run
import pandas as pd
import time
import sys
import os
import argparse

def Cdn(url):
    url = url.rsplit('/')[2]
    cdn = cdnChinaz().run(url)
    if cdn == '未知' or cdn == "" or cdn == 'Failed':
        cdn = cdnFinder().run(url)
    print(f"[+] URL:{url} | CDN:{cdn}")
    return cdn

def portscan(url):
    return portscan_run(url)

def Waf(url):
    url = url.rsplit('/')[2]
    waf = waf_ident_run(url)
    print(f"[+] URL:{url} | WAF:{waf}")
    return waf

def Finger(url):
    banner = finger_run(url)
    cms = banner.get('CMS')
    webframe = banner.get('WEB框架')
    webserver = banner.get('WEB服务器')
    proglang = banner.get('开发语言')
    other = banner.get('其他')

    print(f"[+] URL:{url} | CMS:{cms} | WEB框架:{webframe} | WEB服务器:{webserver} | 开发语言:{proglang} | 其他:{other}")
    return banner

def path(url):
    return dirscan_run(url)

def output(reslist,u_p):
    column = ['URL','标题','CDN', 'WAF', 'CMS', 'WEB框架', 'WEB服务器', '开发语言', '其他', 'PATH', 'PORT']
    filename = time.strftime('%Y_%m_%d_%H_%M', time.localtime(time.time()))
    if not os.path.exists(f'./result'):
        os.makedirs(f'./result')
    for res in reslist:
        res[0] = res[0].split('/')[2]
        res[-2] = f'result/path/{filename}/{res[0]}.txt'
    t = pd.DataFrame(columns=column, data=reslist)
    t.to_csv(f"./result/{filename}.csv",mode="w", encoding='GBK')

    for u,pl in u_p.items():
        u = u.split('/')[2]
        if not os.path.exists(f'./result/path/{filename}/'):
            os.makedirs(f'./result/path/{filename}/')
        with open(f"./result/path/{filename}/{u}.txt","w") as f:
            for p in pl:
                f.write(p+'\n')

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument("-k","--key",help="搜索关键词")
    args = parse.parse_args()
    search = args.key

    reslist = []
    print("========================================资产扫描========================================\n")

    print("[*] 正在进行资产扫描,请耐心等候...")
    ul = crawler_run(search)
    if ul == "None" or len(ul) == 0:
        print("[warning] 未扫描到资产,请尝试更换搜索关键词！")
        sys.exit(-1)
    u_t = assethandle_run(ul)
    urllist = []
    titlelist = []
    for u,t in u_t.items():
        res = []
        res.append(u)
        res.append(t)
        reslist.append(res)

    print("\n========================================CDN识别========================================\n")

    print("[*] 正在进行CDN识别,请耐心等候...")
    cdn = ""
    for res in reslist:
        url = res[0]
        cdn = Cdn(url)
        res.append(cdn)

    print("\n========================================WAF识别========================================\n")

    print("[*] 正在进行WAF识别,请耐心等候...")
    for res in reslist:
        url = res[0]
        waf = Waf(url)
        res.append(waf)

    print("\n========================================指纹识别========================================\n")

    print("[*] 正在进行指纹识别,请耐心等候...")
    for res in reslist:
        url = res[0]
        banner = Finger(url)
        res.append(banner.get('cms'))
        res.append(banner.get('WEB框架'))
        res.append(banner.get('WEB服务器'))
        res.append(banner.get('开发语言'))
        res.append(banner.get('其他'))

    print("\n========================================目录扫描========================================")

    print("[*] 正在进行目录扫描,请耐心等候...")
    u_p = {}
    for res in reslist:
        url = res[0]
        pathlist = path(url)
        u_p[url] = pathlist
        res.append('NONE')

    print("\n========================================端口扫描========================================\n")

    print("[*] 正在进行端口扫描,请耐心等候...")
    for res in reslist:
        url = res[0]
        if cdn == "unknown" or cdn == 'Failed':
            portlist = portscan(url)
        else:
            portlist = ['存在CDN']
            print("[warning] 存在CDN!")
        portlist = str(portlist).strip('[').strip(']').replace("'", "")
        res.append(portlist)

    output(reslist, u_p)
#    res = [url,title,cdn,waf,banner.get('cms'),banner.get('WEB框架'),banner.get('WEB服务器'),banner.get('开发语言'),banner.get('其他'),path,portlist]


