# coding=gbk
from math import log

import pandas as pd

from pymysql_comm import UsingMysql


def selectcompanynum(date):
    with UsingMysql(log_time=True) as um:
        sql = "select student_num,area from student where time <= %s"
        params = (date)
        um.cursor.execute(sql, params)
        return um.cursor.fetchall()


def selectall(time):
    with UsingMysql(log_time=True) as um:
        sql = "select * from stock_list where industry !='软件服务' and list_date <= %s"
        params = (time)
        um.cursor.execute(sql, params)
        return um.cursor.fetchall()


def selectcount(area, time):
    with UsingMysql(log_time=True) as um:
        sql = "select count(1) as num from stock_list where industry !='软件服务' and area = %s and list_date <= %s"
        params = (area, time)
        um.cursor.execute(sql, params)
        return um.cursor.fetchone()


def create_one(data):
    with UsingMysql(log_time=True) as um:
        try:
            sql = "insert into stock_iv(ts_code,iv,time) " + \
                  "values(%s,%s,%s)"
            params = (data['ts_code'], data['iv'], data['time'])
            um.cursor.execute(sql, params)
        except BaseException as e:
            print(e)


data = {
    "安徽": [0, 900, 650, 1300, 1060, 1350, 1170, 1500, 740, 460, 1740, 300, 560, 1571, 140, 370, 1224, 1200, 1250, 1531,
           530, 780, 828, 358, 1260, 800, 2500, 2871, 1620, 350, 1100],
    "北京": [900, 0, 1525, 1200, 1900, 2050, 2100, 2300, 250, 625, 1042, 1050, 1400, 850, 870, 1200, 630, 400, 900, 1400,
           380, 430, 900, 1063, 1500, 80, 2530, 2400, 1700, 1160, 1430],
    "福建": [650, 1525, 0, 1850, 713, 1170, 1290, 1100, 1400, 1100, 2260, 710, 680, 2000, 640, 452, 1800, 1762, 1800,
           2000, 1200, 1500, 1400, 610, 1550, 1450, 2800, 3500, 1700, 450, 1320],
    "甘肃": [1300, 1200, 1850, 0, 1700, 1500, 1080, 1890, 1020, 920, 2200, 1150, 1230, 2030, 1480, 1400, 1820, 880, 340,
           250, 1120, 780, 510, 1730, 600, 1220, 1380, 1600, 1250, 1680, 750],
    "广东": [1060, 1900, 713, 1700, 0, 480, 760, 460, 1680, 1300, 2830, 850, 580, 2600, 1160, 700, 2280, 2000, 1850, 1850,
           1580, 1640, 1300, 1200, 1200, 1800, 2300, 3300, 1100, 1100, 980],
    "广西": [1350, 2050, 1170, 1500, 480, 0, 460, 340, 1800, 1400, 3100, 1040, 760, 2800, 1470, 1020, 2500, 2034, 1770,
           1650, 1780, 1710, 1300, 1600, 960, 1960, 1900, 3000, 620, 1400, 790],
    "贵州": [1170, 2100, 1290, 1080, 760, 460, 0, 780, 1480, 1130, 2800, 880, 680, 2560, 1340, 950, 2230, 1640, 1300,
           1200, 1470, 1350, 840, 1500, 550, 1670, 1550, 2560, 460, 1380, 340],
    "海南": [1500, 2300, 1100, 1890, 460, 340, 780, 0, 2030, 1630, 3200, 1200, 940, 2950, 1556, 1100, 2680, 2300, 2100,
           2030, 1960, 2000, 1560, 1700, 1300, 2200, 2200, 3400, 950, 1460, 1180],
    "河北": [740, 250, 1400, 1020, 1680, 1800, 1480, 2030, 0, 360, 1350, 820, 1100, 1130, 780, 1030, 880, 400, 730, 1200,
           300, 180, 640, 970, 1250, 250, 2400, 2400, 1800, 1000, 1200],
    "河南": [460, 625, 1100, 920, 1300, 1400, 1130, 1630, 360, 0, 1660, 420, 690, 1450, 570, 640, 1200, 750, 780, 1100,
           400, 400, 440, 800, 1000, 600, 2200, 2500, 1480, 780, 850],
    "黑龙江": [1740, 1042, 2260, 2200, 2830, 3100, 2800, 3200, 1350, 1660, 0, 1980, 2260, 250, 1670, 2200, 520, 1280, 1800,
            2300, 1270, 1450, 1950, 1680, 2600, 1060, 3600, 3100, 3200, 1830, 2500],
    "湖北": [300, 1050, 710, 1150, 850, 1040, 880, 1200, 820, 420, 1980, 0, 280, 1780, 480, 200, 1500, 1200, 1150, 1400,
           760, 870, 680, 660, 980, 1000, 2200, 2800, 1250, 560, 750],
    "湖南": [560, 1400, 680, 1230, 580, 760, 680, 940, 1100, 690, 2260, 280, 0, 2080, 730, 280, 1770, 1431, 1300, 1400,
           1040, 1100, 800, 880, 930, 1260, 2200, 2800, 1060, 750, 660],
    "吉林": [1571, 850, 2000, 2030, 2600, 2800, 2560, 2950, 1130, 1450, 250, 1780, 2080, 0, 1450, 1850, 282, 1157, 1700,
           2200, 1070, 1300, 1800, 1400, 2400, 870, 3400, 3000, 2900, 1600, 2300],
    "江苏": [140, 870, 640, 1480, 1160, 1470, 1340, 1556, 780, 570, 1670, 480, 730, 1450, 0, 450, 1120, 1150, 1360, 1630,
           520, 860, 960, 260, 1400, 780, 2600, 3000, 1750, 220, 1200],
    "江西": [370, 1200, 452, 1400, 700, 1020, 950, 1100, 1030, 640, 2200, 200, 280, 1850, 450, 0, 1600, 1400, 1400, 1600,
           850, 1000, 900, 550, 1200, 1160, 2400, 3000, 1400, 440, 900],
    "辽宁": [1224, 630, 1800, 1820, 2280, 2500, 2230, 2680, 880, 1200, 520, 1500, 1770, 282, 1120, 1600, 0, 950, 1460,
           1980, 700, 1057, 1460, 1178, 2200, 570, 3200, 2880, 2630, 1300, 2000],
    "内蒙": [1200, 400, 1762, 880, 2000, 2034, 1640, 2300, 400, 750, 1280, 1200, 1431, 1157, 1150, 1400, 950, 0, 530, 960,
           720, 380, 760, 1400, 1330, 510, 2240, 2000, 1960, 1400, 1300],
    "宁夏": [1250, 900, 1800, 340, 1850, 1770, 1300, 2100, 730, 780, 1800, 1150, 1300, 1700, 1360, 1400, 1460, 530, 0,
           420, 1000, 550, 500, 1670, 900, 980, 1680, 1700, 1530, 1530, 980],
    "青海": [1531, 1400, 2000, 250, 1850, 1650, 1200, 2030, 1200, 1100, 2300, 1400, 1400, 2200, 1630, 1600, 1980, 960,
           420, 0, 1420, 890, 730, 1940, 670, 1300, 1220, 1280, 1300, 1830, 840],
    "山东": [530, 380, 1200, 1120, 1580, 1780, 1470, 1960, 300, 400, 1270, 760, 1040, 1070, 520, 850, 700, 720, 1000,
           1420, 0, 430, 800, 700, 1370, 270, 2500, 2600, 1900, 810, 1200],
    "山西": [780, 430, 1500, 780, 1640, 1710, 1350, 2000, 180, 400, 1450, 870, 1100, 1300, 860, 1000, 1057, 380, 550, 890,
           430, 0, 480, 1060, 1180, 450, 2100, 2170, 1680, 1140, 1020],
    "陕西": [828, 900, 1400, 510, 1300, 1300, 840, 1560, 640, 440, 1950, 680, 800, 1800, 960, 900, 1460, 760, 500, 730,
           800, 480, 0, 1200, 630, 880, 1820, 2080, 1180, 1120, 580],
    "上海": [358, 1063, 610, 1730, 1200, 1600, 1500, 1700, 970, 800, 1680, 660, 880, 1400, 260, 550, 1178, 1400, 1670,
           1940, 700, 1060, 1200, 0, 1660, 980, 2800, 3500, 1870, 200, 1340],
    "四川": [1260, 1500, 1550, 600, 1200, 960, 550, 1300, 1250, 1000, 2600, 980, 930, 2400, 1400, 1200, 2200, 1330, 900,
           670, 1370, 1180, 630, 1660, 0, 1500, 1200, 2050, 670, 1500, 340],
    "天津": [800, 80, 1450, 1220, 1800, 1960, 1670, 2200, 250, 600, 1060, 1000, 1260, 870, 780, 1160, 570, 510, 980, 1300,
           270, 450, 880, 980, 1500, 0, 2600, 2500, 2050, 1000, 1400],
    "西藏": [2500, 2530, 2800, 1380, 2300, 1900, 1550, 2200, 2400, 2200, 3600, 2200, 2200, 3400, 2600, 2400, 3200, 2240,
           1680, 1220, 2500, 2100, 1820, 2800, 1200, 2600, 0, 1600, 1260, 2750, 1530],
    "新疆": [2871, 2400, 3500, 1600, 3300, 3000, 2560, 3400, 2400, 2500, 3100, 2800, 2800, 3000, 3000, 3000, 2880, 2000,
           1700, 1280, 2600, 2170, 2080, 3500, 2050, 2500, 1600, 0, 2500, 3300, 2300],
    "云南": [1620, 1700, 1700, 1250, 1100, 620, 460, 950, 1800, 1480, 3200, 1250, 1060, 2900, 1750, 1400, 2630, 1960,
           1530, 1300, 1900, 1680, 1180, 1870, 670, 2050, 1260, 2500, 0, 1760, 630],
    "浙江": [350, 1160, 450, 1680, 1100, 1400, 1380, 1460, 1000, 780, 1830, 560, 750, 1600, 220, 440, 1300, 1400, 1530,
           1830, 810, 1140, 1120, 200, 1500, 1000, 2750, 3300, 1760, 0, 1310],
    "重庆": [1100, 1430, 1320, 750, 980, 790, 340, 1180, 1200, 850, 2500, 750, 660, 2300, 1200, 900, 2000, 1300, 980, 840,
           1200, 1020, 580, 1340, 340, 1400, 1530, 2300, 630, 1310, 0]
}
df = pd.DataFrame(data,
                  index=["安徽", "北京", "福建", "甘肃", "广东", "广西", "贵州", "海南", "河北", "河南", "黑龙江", "湖北", "湖南", "吉林", "江苏",
                         "江西", "辽宁", "内蒙", "宁夏", "青海", "山东", "山西", "陕西", "上海", "四川", "天津", "西藏", "新疆", "云南", "浙江",
                         "重庆"])
print(df.loc['安徽', '北京'])

for time in range(2009, 2020):
    time = str(time)
    for stock in selectall(time):
        mid = 0
        count = selectcount(stock['area'], time)['num']
        for info in selectcompanynum(time):
            if stock['area'] != info['area']:
                mid = mid + int(info['student_num']) / (3 * df.loc[stock['area'], info['area']])
            else:
                mid = mid + int(info['student_num']) / 3
        data = {"iv": str(mid/count), "ts_code": stock['symbol'], "time": time}
        create_one(data)
