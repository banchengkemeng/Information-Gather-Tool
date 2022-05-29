import requests

class cdnChinaz():

    def run(self,key):
        url = 'https://cdn.chinaz.com/ajax/GetCdnAboutInfo'

        header = {
            "Content-Type":"application/x-www-form-urlencoded",
        }

        datas = {
            "prov":"",
            "host":key,
            "tab":"q",
            "typeId":"3",
            "isDefault":"0"
        }
        cnt = 0
        while True:
            try:
                resp = requests.post(url,headers=header,data=datas)
                if resp.json().get('total') != 0:
                    return resp.json().get('companyName')
                else:
                    return ""
            except:
                cnt = cnt + 1
                if cnt > 2:
                    print("![ERROR] cdnident.cdnChinaz.run")
                    return 'Failed'

# if __name__ == '__main__':
#     key = "www.bilibili.com",
#     getCdn()