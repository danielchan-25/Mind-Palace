import os.path
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import json
import csv
import datetime
# ------------------------------- #
# 日期: 2023/6/29
# 作者: cc
# 功能：每日获取指定英雄的最低战力信息
# 注意：调用了api.txapi.cn 接口
# ------------------------------- #
if not os.path.exists('战力查询\\'):
    os.mkdir('战力查询\\')

today = datetime.datetime.today().date()
hero_list = ['李白','娜可露露','杨戬','花木兰','达摩','鲁班七号','亚瑟','不知火舞']
# ---------------------------------------------------------------------------------------- #
def create_csv_file():
    csv_title = ['英雄名称', '平台', '最低的县标所在位置', '最低的县标所需战力', '最低的市标所在位置',
                 '最低的市标所需战力', '最低的省标所在位置', '最低的省标所需战力', '最低的国标所需战力', '更新时间']

    for hero_name in hero_list:
        csv_file = open(f'战力查询\\{hero_name}.csv','w',newline='')
        for title in csv_title:
            csv_file.write(str(title)+',')
        csv_file.write('\n')
        csv_file.close()
# ---------------------------------------------------------------------------------------- #
def get_Data():
    for hero_name in hero_list:
        api_url = f'http://api.txapi.cn/v1/c/game_query/wz?token=0M1Y2WCmYMxt2&type=iwx&hero={hero_name}'
        response = requests.get(url=api_url)
        data = json.loads(response.text)['data']

        with open(f'战力查询\\{hero_name}.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data.values())
        print(f'{hero_name} 的数据已写入')
    print(f'已将 {today} 的数据写入，等待明天的 09:10 继续执行\n# ----------------------------------------- #')
# ---------------------------------------------------------------------------------------- #
print('''
# ----------------------------------------- #
程序将在 09:10 自动执行
详细数据见：战力查询 文件夹

:)
# ----------------------------------------- #
''')

if not os.path.exists('战力查询\\'):
    os.mkdir('战力查询\\')
    create_csv_file()
# ---------------------------------------------------------------------------------------- #
# 定时任务
sched = BlockingScheduler()
sched.add_job(get_Data,'cron',hour=9,minute=10,timezone='Asia/Shanghai')
sched.start()