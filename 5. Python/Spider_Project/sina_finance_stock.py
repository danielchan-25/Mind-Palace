# -*- coding: utf-8 -*-
import json
import datetime
import requests
import schedule
import time
from bs4 import BeautifulSoup


# 日期: 2024-05-27
# 作者: Alex
# 功能: 爬取新浪财经中，股票栏目的信息，每个整点和半点运行。

def get_html_response(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.text


def get_html_content(response, html_label, html_class):
    soup = BeautifulSoup(response, 'html.parser')
    result = soup.find_all(html_label, class_=html_class)
    return result


def main():
    url = 'https://finance.sina.cn/stock/?vt=4&cid=76699&node_id=76699'
    html_data = get_html_response(url)

    title_list = [i.text.split() for i in get_html_content(html_data, 'h2', 'm_f_con_t cm_tit')]
    link_list = [i['href'] for i in get_html_content(html_data, 'a', 'f_card m_f_a_r')]

    data = []

    for i, j in zip(title_list, link_list):
        html_data = get_html_response(j)
        content_time = [a['content'] for a in
                        BeautifulSoup(html_data, 'html.parser').find_all('meta', property='article:published_time')]
        content_list = [b.text.split() for b in get_html_content(html_data, 'p', 'art_p')]
        content = [c[0] for c in content_list if c]
        result = {"time": ' '.join(content_time), "title": ' '.join(i), "content": ' '.join(content)}
        data.append(result)

    with open(f'{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}_sina.txt', mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


schedule.every().hour.at(":00").do(main)
schedule.every().hour.at(":30").do(main)

while True:
    schedule.run_pending()
    time.sleep(59)
