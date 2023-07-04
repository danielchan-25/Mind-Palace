import json
import os.path
import time
import requests
import urllib
from urllib import parse
# --------------------------------------- #
# 日期：2023/7/3
# 作者：cc
# 获取所有英雄的壁纸
# --------------------------------------- #
if not os.path.exists('英雄壁纸\\'):
    os.mkdir('英雄壁纸\\')

for page_number in range(0,35):
    url = f'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={page_number}&iOrder=0&iSortNumClose=1&jsoncallback=jQuery1113006142795572034143_1688369295119&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1688369295123'
    headers = {
        'Cookie':'请填入自己的Cookie',
        'Referer':'https://pvp.qq.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers).text
    html = response[43:-2]
    json_str = json.loads(html)
    image_list = json_str['List']
    print(f'正在下载第 {page_number} 页的照片')
    for i in image_list:
        time.sleep(2)
        print(f'本页共 {len(i)} 张照片，正在下载...')
        old_url = i['sProdImgNo_8']
        new_url = urllib.parse.unquote(old_url)
        resolution_ratio = new_url.split('/200',1)[0]       # 分辨率
        sProdName = i['sProdName']
        image_name = urllib.parse.unquote(sProdName)
        url = f'{resolution_ratio}/0'
        image_response = requests.get(url=url)
        with open(f'英雄壁纸\\{image_name}.jpg','wb') as file:
            file.write(image_response.content)
print(f'下载完毕，请查看：英雄壁纸文件夹')