# -*- coding: UTF-8 -*-
import socket
from urllib.parse import urlparse
import socket
from gevent import monkey
# monkey.patch_all()
import gevent
import gevent.pool

def get_Iplist(domain):  # 获取域名解析出的IP列表
    url = urlparse(domain).netloc
    print(url)
    ip_list = []
    try:
        adders = socket.getaddrinfo(url, None)
        for item in adders:
            if item[4][0] not in ip_list:
                if ':' not in item[4][0]: #去掉ipv6地址
                    ip_list.append(item[4][0])
    except Exception as e:
        pass
    return ip_list

def scan_port(ip):
    g = gevent.pool.Pool(100) #设置线程数
    run_list = []
    iplist = [
        5,8,9,20, 21, 22, 23, 25, 53, 69, 81, 82, 83, 84, 85, 86, 87, 88, 89, 443, 110,111, 2049, 137, 139, 445, 143, 161, 389,
        512, 513, 514, 873, 1194, 1352, 1433, 1521, 1500, 1723, 2082, 2083, 2181, 2601, 2604, 3128, 3312, 3311, 3306,
        3389, 3690, 4848, 5000, 5432, 5900, 5901, 5984, 6379, 7001, 7002, 7778, 8000, 8443, 8069, 8080,8081,8082,8083,
        8084,8085,8086,8087,8088,8089,9080,9081,9200,
        9300, 11211, 27017, 27018, 50070, 50030
    ]
    for port in iplist:
        run_list.append(g.spawn(TCP_connect,ip,port))
    gevent.joinall(run_list)

def TCP_connect(ip,port):
    TCP_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    TCP_sock.settimeout(0.5)  #设置连接超时
    try:
        result = TCP_sock.connect_ex((ip,int(port)))
        if result == 0:
            print(f"[+] {ip}:{port} => open")
            portlist.append(str(port))
        else:
            pass
        TCP_sock.close()
    except socket.error as e:
        pass

def portscan_run(url):
    url = url.split('/')[2]
    url = url.strip('\n')
    if url[0].isdigit():
        ip = url
    else:
        ip = socket.gethostbyname(url)
    global portlist
    portlist = []
    scan_port(ip)
    portlist.sort()
    print(f"[+] 开放端口:{','.join(portlist)}\n")
    return portlist

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    portscan_run(url)