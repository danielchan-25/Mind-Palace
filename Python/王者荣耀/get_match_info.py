import os.path
import requests
import json

if not os.path.exists('赛事\\赛事数据.csv'):
    os.mkdir('赛事\\')
    csv_title = '比赛id,队伍1,队伍2,队伍1得分,队伍2得分,开始时间,结束时间,比赛地址,比赛类型'
    file = open('赛事\\赛事数据.csv','w',newline='')
    file.write(csv_title+'\n')
    file.close()

url = 'https://prod.comp.smoba.qq.com/leaguesite/matches/open?league_id=20230002'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.get(url,headers)
html = json.loads(response.text)
data = html['results']
for i in data:
    match_date = i['match_id']
    camp1 = i['camp1']['team_name']
    camp2 = i['camp2']['team_name']
    camp1_score = i['camp1']['score']
    camp2_score = i['camp2']['score']
    start_time = i['start_time']
    end_time = i['end_time']
    match_address = i['match_address']
    match_stage_desc = i['match_stage_desc']
    # print(match_date,camp1,camp2,camp1_score,camp2_score,start_time,end_time,match_address,match_stage_desc)

    csv_title = '比赛id,队伍1,队伍2,队伍1得分,队伍2得分,开始时间,结束时间,比赛地址,比赛类型'
    file = open('赛事\\赛事数据.csv','a',newline='')
    file.write(f'{match_date},{camp1},{camp2},{camp1_score},{camp2_score},{start_time},{end_time},{match_address},{match_stage_desc}\n')
file.close()