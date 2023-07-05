from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
# ------------------------------------------- #
# 日期：2023年7月5日
# 作者：cc
# 功能：获取近年来KPL赛事的比赛城市，以词云的方式展示
# ------------------------------------------- #
def get_Data():
    # 读取数据
    csv_file = '赛事\\赛事数据.csv'
    with open(csv_file,'r',newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        address_list =  [row[-2] for row in reader]
    address = ' '.join(address_list)
    return address

# 生成词云
wc = WordCloud(
    font_path='msyh.ttc',
    width = 500,
    height= 400,
    max_font_size = 500,
    min_font_size = 50,
    background_color = 'white'
)
wc.generate(get_Data())

# 展示
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()