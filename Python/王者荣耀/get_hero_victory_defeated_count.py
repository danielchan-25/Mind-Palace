import csv
import os
# --------------------------------------------- #
# 日期：2023年7月5日
# 作者：cc
# 功能：获取KPL赛事中，胜利/失败场数最多的英雄
# 注意：运行程序前，请先运行：get_hero_match_data.py
# --------------------------------------------- #
csv_file_list = []
for i in os.listdir('赛事\\'):
    if i != '赛事数据.csv':
        csv_file_list.append(i)

def find_max_victory_hero(csv_file):
    match_name = csv_file.split('.',-1)[0]

    max_victory_count = 0
    max_defeated_count = 0
    max_win_rate = float("0.0")
    victory_hero_name = ""
    defeated_hero_name = ""
    win_rate_name = ""

    with open(f'赛事\\{csv_file}','r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            hero_name = row[0]
            victory_count = int(row[4])             # 胜场列
            defeated_count = int(row[5])            # 败场列
            # win_rate = float(row[6])                # 英雄胜率

            if victory_count > max_victory_count:
                max_victory_count = victory_count
                victory_hero_name = hero_name
                win_rate = row[6]

            if defeated_count > max_defeated_count:
                max_defeated_count = defeated_count
                defeated_hero_name = hero_name
                lose_rate = row[6]

    print(f'在{match_name}中，\n'
          f'胜场次数最多的英雄是：{victory_hero_name}，胜利场数为：{max_victory_count} 场，胜率为：{win_rate}；\n'
          f'失败次数最多的英雄是：{defeated_hero_name}，失败场数为：{max_defeated_count} 场，胜率为：{lose_rate}。\n\n')

for csv_file in csv_file_list:
    find_max_victory_hero(csv_file = csv_file)