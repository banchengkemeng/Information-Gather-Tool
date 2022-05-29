import json
import requests
import re
from lxml import etree

class cdnFinder():

    def run(self,key):

        url_Auth = 'https://www.cdnplanet.com/tools/cdnfinder/'

        header_Auth = {
            "Sec-Ch-Ua": '(Not(A:Brand";v="8", "Chromium";v="101"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }

        cookie_Auth = {
            "_ga": "GA1.2.370430653.1652453523",
            "_gid": "GA1.2.1561857774.1652453523"
        }
        cnt = 0
        while True:
            try:
                resp = requests.get(url_Auth, headers=header_Auth, cookies=cookie_Auth)
                data = etree.HTML(resp.text)
                auth = data.xpath("//script[@id='_cdnp']/text()")
                auth = re.findall(r'.*Token = "(.*?)".*', str(auth))
                Auth = auth[0]
                break

            except:
                cnt = cnt + 1
                if cnt > 2:
                    print("![ERROR] cdnident.cdnFinder.getAuth")
                    return 'Failed'

        url_Id = 'https://api.cdnplanet.com/tools/cdnfinder?lookup=hostname-or-url'

        header_Id = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": Auth,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
        }

        datas = {
            "query": key
        }

        cnt = 0
        while True:
            try:
                resp = requests.post(url_Id, headers=header_Id, data=json.dumps(datas))
                id = resp.json().get('id')
                break
            except:
                cnt = cnt + 1
                if cnt > 2:
                    print("![ERROR]: cdnident.cdnFinder.getid")
                    return 'Failed'

        cnt = 0
        while True:
            try:
                header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
                    "referer": "https://www.cdnplanet.com/tools/cdnfinder/"
                }
                url = f'https://api.cdnplanet.com/tools/results?source=website&service=cdnfinder&id={id}'
                resp = requests.get(url,headers=header)
                return resp.json().get('results')[0].get('cdn')
            except:
                cnt = cnt + 1
                if cnt > 2:
                    print("![ERROR]: cdnident.cdnFinder.getCdn")
                    return 'Failed'

# c = cdnFinder().run("www.cdnplanet.com")
# print(c)
# if __name__ == '__main__':
#     key = "www.qq.com"
#     cdnident = getCdn(getid(key))
#     print(cdnident)
