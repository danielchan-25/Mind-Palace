import os.path
import time
import requests
import json
# ------------------------------ #
# 日期：2023年7月5日
# 作者：cc
# 功能：获取 KPL 赛事中英雄的数据
# ------------------------------ #
if not os.path.exists('赛事\\'):
    os.mkdir('赛事\\')

def get_Data():
    csv_title = '英雄,出场次数,禁用次数,被禁用率,胜场次数,败场次数,胜率,场均击杀数,场均助攻数,场均死亡数,场均kda,场均收益,场均比赛时长'

    url = 'https://prod.comp.smoba.qq.com/leaguesite/leagues/open'
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    league_id_list = json_data['results']
    for i in league_id_list:
        league_id = i['league_id']
        file_name = i['league_name']
        with open(f'赛事\\{file_name}.csv','w',newline='') as file:
            file.write(csv_title+'\n')
        print(f'正在写入 {file_name} 数据')

        # ------------------------------------------------------------------------------------------------------ #
        url = f'https://prod.comp.smoba.qq.com/leaguesite/league/hero/settle_list/open?league_id={league_id}'
        response = requests.get(url=url)
        json_str = json.loads(response.text)['data']
        for j in json_str:
            hero_name = j['hero_info']['hero_name']                                     # 英雄名称
            battle_count = j['statistics_info']['battle_count']                         # 出场次数
            ban_num = j['bp_statistics_info']['ban_num']                                # 禁用次数
            ban_rate = j['bp_statistics_info']['ban_rate']                              # 禁用率
            victory_battle_count = j['statistics_info']['victory_battle_count']         # 胜场次数
            defeated_battle_count = j['statistics_info']['defeated_battle_count']       # 败场次数
            win_rate = j['statistics_info']['win_rate']                                 # 胜率
            avg_kill_num = j['statistics_info']['avg_kill_num']                         # 场均击杀数
            avg_assist_num = j['statistics_info']['avg_assist_num']                     # 场均助攻数
            avg_death_num = j['statistics_info']['avg_death_num']                       # 场均死亡数
            avg_kda = j['statistics_info']['avg_kda']                                   # 场均kda
            avg_gold = j['statistics_info']['avg_gold']                                 # 场均收益
            avg_game_duration = j['statistics_info']['avg_game_duration']               # 场均比赛时长
            data = f'{hero_name},{battle_count},{ban_num},{ban_rate},{victory_battle_count},{defeated_battle_count},{win_rate},' \
                   f'{avg_kill_num},{avg_assist_num},{avg_death_num},' \
                   f'{avg_kda},{avg_gold},{avg_game_duration}\n'
            with open(f'赛事\\{file_name}.csv','a',newline='') as file:
                file.write(data)
        time.sleep(5)

if __name__ == '__main__':
    get_Data()