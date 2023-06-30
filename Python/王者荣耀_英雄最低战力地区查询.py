import requests
import json
import csv
import datetime
# --------------------------------------- #
# 日期: 2023/6/29
# 作者: cc
# 功能：获取王者荣耀最低战力
# 注意：第一次运行，请运行 create_File 函数
# --------------------------------------- #

today = datetime.datetime.today().date()
csv_file = '王者荣耀最低战力排行.csv'

def create_File():
    file = open(csv_file,'w')
    file.write(str('英雄名称,平台,最低的县标所在位置,最低的县标所需战力,最低的市标所在位置,最低的市标所需战力,最低的省标所在位置,最低的省标所需战力,最低的国标所需战力,更新时间'))


def get_Data():
    # 需要查询的英雄名称
    hero_list = ['李白','娜可露露','杨戬','花木兰','达摩','鲁班七号']
    for hero_name in hero_list:
        api_url = f'http://api.txapi.cn/v1/c/game_query/wz?token=0M1Y2WCmYMxt2&type=iwx&hero={hero_name}'
        response = requests.get(url=api_url)
        data = json.loads(response.text)['data']

        with open(csv_file,'a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data.values())
        print(f'{hero_name} 的数据已写入')

    print(f'{today} 的数据已写入完毕，等待明天数据更新')

get_Data()