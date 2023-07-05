import requests
import json
# --------------------- #
# 日期：2023年7月5日
# 作者：cc
# 功能：获取英雄的信息
# --------------------- #
headers = {
    'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br'
}
url = 'https://pvp.qq.com/zlkdatasys/yuzhouzhan/list/heroList.json?t=1688565355373'
response = requests.get(url,headers)
json_str = json.loads(response.text)
for i in json_str['yzzyxs_4880']:
    address = i['zyyx_9680']
    hero_name = i['yzzyxm_4588']
    hero_id = i['yzzyxi_2602']
    hero_type = i['yzzyxz_1918']
    hero_title = i['yzzyxc_4613']
    data = [address,hero_type,hero_id,hero_title,hero_name]
    print(data)
