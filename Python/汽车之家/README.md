# 汽车之家
> 日期：2023年7月6日
> 
> 作者：cc
## 背景
最近刚考完驾照，心痒痒的想购入一辆小轿车，可是对汽车的了解甚少，只知道那几个牌子，对汽车的各种版本，各种配置一窍不通。

朋友推荐了几辆车：**本田思域、本田型格、马自达3昂克塞拉、丰田卡罗拉**，说这些都适合我

所以打算使用爬虫，抓取一下网上对这几辆车的评价都怎样。

我需要的数据：

- 型号：一辆车分为很多型号，例如什么豪华版什么版什么版等的，各个版本之间相差的不少，这个也要
- 裸车价：4S店的直接销售价格（裸车价=厂家指导价-优惠价格）
- 购车时间：车辆购买的时间
- 购车地点：车辆购买的地点
- 行驶公里数：汽车行驶的总公里数
- 百公里油耗：车辆在道路上按一定速度行驶一百公里的油耗

很重要的一点：**裸车价**，如果超了我的预算范围就不再考虑 T_T

## 流程
