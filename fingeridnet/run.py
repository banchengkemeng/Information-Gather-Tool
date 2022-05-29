from .Wappalyzer import Wappalyzer, WebPage
import csv,os,json
from .whatcms.whatcms import getwhatcms

def finger_run(url):

    # 别直接赋NULL
    all = dict(WEB框架='', WEB服务器='', 开发语言='', CMS='', 其他='')

    #输出WEB指纹的内容
    webpage = WebPage.new_from_url(url)
    wappalyzer = Wappalyzer.latest()
    result=wappalyzer.analyze_with_versions_and_categories(webpage)
    for i in result:
        version = str(result.get(i)['versions'])[1:-1]
        if('Web servers' in str(result.get(i)['categories'])):
            all['WEB服务器']+=i+version+" "
        elif('Programming languages' in str(result.get(i)['categories'])):
            all['开发语言']+=i+version+" "
        elif('Web frameworks' in str(result.get(i)['categories'])):
            all['WEB框架']+=i+version+" "
        elif('CMS' in str(result.get(i)['categories'])):
            all['CMS']+=i+version+" "
        else:
            all['其他']+=i+version+" "

    #如果Wappalyzer没有探测到，就调用第二个工具whatcms
    whatcms = json.dumps(getwhatcms(url))
    if all['开发语言']=="":
        if 'aspx' in whatcms:
            all['开发语言']='aspx'
        elif 'php' in whatcms:
            all['开发语言']='php'
        elif 'jsp' in whatcms:
            all['开发语言']='jsp'
        elif 'asp' in whatcms:
            all['开发语言']='asp'
        elif 'python' in whatcms:
            all['开发语言']='python'
        else:
            all['开发语言']='NULL'

    if all['WEB服务器']=="":
        try:
            all['WEB服务器'] = dict(json.loads(whatcms)).get('server')
        except:
            all['WEB服务器'] = "NULL"
    #把空值变成NULL
    for i in all:
        if all[i] == "":
            all[i] = "NULL"

    return all

if __name__ == '__main__':
    print(finger_run("https://www.baidu.com"))