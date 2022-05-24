# coding=gbk
from pymysql_comm import UsingMysql

# 新增单条记录
def create_one(data):

    with UsingMysql(log_time=True) as um:
        try:
            sql = "insert into adminer_list(ts_code,edu,begin_date,end_date) " + \
                  "values(%s,%s,%s,%s)"
            params = (data['ts_code'],data['edu'],data['begin_date'],data['end_date'])
            um.cursor.execute(sql, params)
        except BaseException as e:
            print(e)

import re
# 导入tushare
import tushare as ts
import stock_list

# 初始化pro接口
pro = ts.pro_api('809e1cd982cabb44bcf52bb954e665438df8b1c84191e6aaf70dbf1c')
import time
if __name__ == '__main__':
    stocks = stock_list.select_all()
    for stock in stocks:
        # 拉取数据
        time.sleep(0.5)
        df = pro.stk_managers(**{
            "ts_code": stock['ts_code'],
            "ann_date": "",
            "start_date": 20090101,
            "end_date": 20200101,
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "edu",
            "begin_date",
            "end_date"
        ])
        for index, row in df.iterrows():
            if row['edu'] == '本科':
                row['edu'] = 2
            elif row['edu'] == '专科':
                row['edu'] = 1
            elif row['edu'] == '硕士':
                row['edu'] = 3
            elif row['edu'] == '博士':
                row['edu'] = 4
            else:
                row['edu'] = 0
            data = {
                'ts_code':row['ts_code'],
                'edu':row['edu'],
                'begin_date':row['begin_date'],
                "end_date": row['end_date']
            }
            create_one(data)


