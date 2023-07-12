import os.path
import requests
import json
# --------------------- #
# 日期：2023年7月5日
# 作者：cc
# 功能：获取英雄的信息
# --------------------- #
if not os.path.exists('英雄信息\\'):
    os.mkdir('英雄信息\\')
hero_name_file = '英雄信息\\hero_name.csv'

def get_Data():
    headers = {
        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    url = 'https://pvp.qq.com/zlkdatasys/yuzhouzhan/list/heroList.json?t=1688565355373'
    response = requests.get(url,headers)
    json_str = json.loads(response.text)
    for i in json_str['yzzyxs_4880']:
        hero_name = i['yzzyxm_4588']
        with open(hero_name_file,'a',newline='') as file:
            file.write(hero_name+'\n')-
    print(f'已将所以英雄名字写入至 {hero_name_file}')

if __name__ == '__main__':
    get_Data()