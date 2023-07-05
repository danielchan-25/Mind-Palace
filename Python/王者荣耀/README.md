# 王者荣耀

> 日期：2023/6/28
>
> 作者：cc

## 背景

本人也是一位王者荣耀玩家，玩这个游戏已经 7 年了，连省标都没有

所以想关注一下：常用英雄省标最低要多少分，尝试拿一个省标 T_T

## 流程

1. 抓取历史 KPL 赛事上的所有英雄数据（√）
   1. 查看哪几位英雄的胜利场数最多，那就先待定选择这几位英雄（√）
   2. 查看哪几位英雄的失败场数最多，避免选择这些英雄（√）
2. 每天抓取这几位英雄的战力，查看哪个地区的分数最低，且出现频率最高，持续观察一个月（ing）

## 代码说明

- `get_hero_match_data.py`：获取 KPL 赛事中英雄的数据
- `get_hero_victory_defeated_count.py`：获取 KPL 赛事中胜场/败场次数最多的英雄
- `get_hero_zhanli_daily.py`：每天定时获取指定英雄的最低战力地区+分数
- `get_match_info.py`：获取近期的 KPL 赛事

## 结论

| 比赛                   | 胜场次数最多的英雄 | 败场次数最多的英雄 |
| ---------------------- | ------------------ | ------------------ |
| 2021KPL春季赛          | 廉颇               | 吕布               |
| 2021KPL春季赛季前赛    | 猪八戒             | 廉颇               |
| 2021KPL秋季赛          | 公孙离             | 沈梦溪             |
| 2021世界冠军杯         | 沈梦溪             | 鲁班大师           |
| 2021年王者荣耀挑战者杯 | 澜                 | 镜                 |
| 2022年KPL夏季赛        | 沈梦溪             | 沈梦溪             |
| 2022年KPL春季赛        | 吕布               | 夏侯惇             |
| 2022年王者荣耀挑战者杯 | 公孙离             | 宫本武藏           |
| 2023年KPL夏季赛        | 公孙离             | 王昭君             |
| 2023年KPL春季赛        | 沈梦溪             | 公孙离             |

近两年来的数据显示

- 我应该选择：**沈梦溪、公孙离、吕布、澜** 这几位英雄进行上分
- 我应该避免选择：**夏侯惇、宫本武藏、王昭君、鲁班大师**

但由于英雄调整时时刻刻都在发生，

## 其它

- `get_hero_image.py`：获取所有英雄皮肤的高清壁纸
- `get_match_city.py`：获取近期 KPL 赛事的比赛城市，查看哪个城市举行的 KPL 赛事最多

---

## 附图

### 获取官网中所有英雄皮肤的高清壁纸

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Python/img/wzry_hero_image.png)

### 获取 KPL 赛事中英雄的数据

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Python/img/wzry_match_hero_data-1.png)

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Python/img/wzry_match_hero_data-2.png)

### 获取 KPL 赛事中胜场/败场次数最多的英雄

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Python/img/wzry_match_hero_victory_defeated_count.png)

### 每天定时获取指定英雄的最低战力地区+分数

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Python/img/wzry_zhanli-1.png)

### 获取近期 KPL 赛事的比赛城市

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Python/img/wzry_match_city.png)

### 获取近期的 KPL 赛事

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Python/img/wzry_match_data-1.png)
