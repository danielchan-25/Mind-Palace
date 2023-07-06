import os.path
import requests
import json
import time
from lxml import etree
# ---------------------------- #
# 日期：2023年7月6日
# 作者：cc
# 功能：获取本田思域车主的评价
# ---------------------------- #
csv_file_name = '本田思域网评.csv'
if not os.path.exists(csv_file_name):
    with open(csv_file_name,'w',newline='') as file:
        file.write(f'发表时间,车型,裸车价,购买时间,购买地点,行驶公里,百公里油耗(L),综合评分,满意,不满意\n')

def get_Data(page_number):
    url = f'https://koubeiipv6.app.autohome.com.cn/pc/series/list?pm=3&seriesId=135&pageIndex={page_number}&pageSize=20&yearid=0&ge=0&seriesSummaryKey=0&order=1'
    response = requests.get(url)
    json_str = json.loads(response.text)
    for i in json_str['result']['list']:
        postid = i['showId']                # 帖子id
        posttime = i['posttime']            # 发帖时间
        specname = i['specname']            # 汽车型号
        buyprice = i['buyprice']            # 裸车价
        boughtDate = i['boughtDate']        # 购买日期
        buyplace = i['buyplace']            # 购买价格
        distance =i['distance']             # 行驶公里
        actual_oil_consumption = i['actual_oil_consumption']            # 百公里油耗
        averageScore = i['averageScore']                                # 综合评价

        # 从帖子中爬取评价
        post_url = f'https://k.autohome.com.cn/detail/view_{postid}.html'
        user_view_response = requests.get(post_url)
        html = etree.HTML(user_view_response.text)
        # 最满意
        feel_good = html.xpath(
            '//div[@class="satisfied kb-item"]/p[@class="kb-item-msg"]//text()')
        # 最不满意
        feel_bad = html.xpath(
            '//div[@class="unsatis kb-item"]/p[@class="kb-item-msg"]//text()')

        # 输出显示
        print(f'正在爬取 {post_url} 的数据')

        # 数据拼接
        data = f'{posttime},{specname},{buyprice},{boughtDate},{buyplace},{distance},{actual_oil_consumption},{averageScore}\n'
        # data = f'{posttime},{specname},{buyprice},{boughtDate},{buyplace},{distance},{actual_oil_consumption},{",".join(feel_good)},{",".join(feel_bad)},{averageScore}\n'
        file = open(csv_file_name,'a')
        file.write(data)
        file.close()

for number in range(0,200):
    time.sleep(5)
    get_Data(page_number=number)
    print(f'正在爬取第 {number} 页的数据')