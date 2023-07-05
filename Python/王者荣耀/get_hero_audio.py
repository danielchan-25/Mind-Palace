import requests
import json
# --------------------- #
# 日期：2023年7月5日
# 作者：cc
# 功能：获取英雄的语音
# --------------------- #
url = 'https://pvp.qq.com/zlkdatasys/data_zlk_lb.json?callback=createList'
headers = {
    'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding':'gzip, deflate, br'
}
response = requests.get(url,headers)
json_str = json.loads(response.text[11:-1])['yylb_34']
for i in json_str:
    hero_id = i['yxid_a7']
    print(hero_id)
    for j in i['yy_4e']:
        print(j['yywa1_f2'])
