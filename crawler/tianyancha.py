# -*- coding: UTF-8 -*-
import sys
import tldextract
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def tianyancha_run(key):

    headers = {
        'Cookie': 'csrfToken=VtbnK1tn9NoUb0fUqHVlS0Xc; jsid=SEM-BAIDU-PZ0824-SY-000001; bannerFlag=false; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1600135387; show_activity_id_4=4; _gid=GA1.2.339666032.1600135387; relatedHumanSearchGraphId=23402373; relatedHumanSearchGraphId.sig=xQxyUIDqVdMkulWk5m_htP28Pzw8_eM8tUMIyK4_qqs; refresh_page=0; RTYCID=69cd6d574b1c4116995bab3fd96a9466; CT_TYCID=a870d4ebb91849b094668d1d969c7702; token=899079c4b21e4d22916083d22f72e1e3; _utm=dac53239b45f49709262be264fd289f3; cloud_token=bb4c875aed794641966b7f7536187e80; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1600147199; _gat_gtag_UA_123487620_1=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    url = f'https://www.tianyancha.com/search?key={key}'
    cnt = 0
    while True:
        try:
            html = requests.get(url, headers=headers,timeout=3)
            soup = BeautifulSoup(html.text, 'lxml')
            info = soup.select('.result-list .content a')[0] #只搜索了第一个显示的第一个公司名称

            company_url = info['href']	#天眼查搜索企业后进入的页面网址

            html_detail = requests.get(company_url, headers=headers)
            soup_detail = BeautifulSoup(html_detail.text, 'lxml')

            data_infos = soup_detail.find('a', class_='company-link')	#找到网址的位置
            if data_infos is None:
                return "None"
                # print('None')
            else:
                # data_email = soup_detail.find('div', class_='in-block sup-ie-company-header-child-2 copy-info-box').find_all('span')[4] #找到邮箱的位置
                # email = data_email.text
                domain = tldextract.extract(data_infos.text).registered_domain
                # print(f'[+] {domain}')      # 输出
                return domain
        except:
            cnt = cnt + 1
            if cnt > 2:
                # print("None")
                return "None"

