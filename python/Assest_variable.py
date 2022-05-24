# coding=gbk
from pymysql_comm import UsingMysql

def exit(ts_code,ann_date,ann_type):
    with UsingMysql(log_time=True) as um:
        sql = "select * from assets_list where ts_code = %s and ann_date = %s and ann_type = %s"
        params = (ts_code,ann_date,ann_type)
        um.cursor.execute(sql, params)
        data = um.cursor.fetchone()
        if data is None:
            print(ts_code + "不存在")
            return False
        else:
            print(ts_code + "已存在")
            return True

# 新增单条记录
def create_one(data):

    with UsingMysql(log_time=True) as um:
        try:
            sql = "insert into assets_list(ts_code,assets,time) " + \
                  "values(%s,%s,%s)"
            params = (data['ts_code'],data['assets'],data['time'])
            um.cursor.execute(sql, params)
        except BaseException as e:
            print(e)

import re
# 导入tushare
import tushare as ts
import stock_list

# 初始化pro接口
pro = ts.pro_api('809e1cd982cabb44bcf52bb954e665438df8b1c84191e6aaf70dbf1c')

if __name__ == '__main__':
    stocks = stock_list.select_all()
    for stock in stocks:
        # 拉取数据
        df = pro.balancesheet(**{
            "ts_code": stock['ts_code'],
            "ann_date": "",
            "f_ann_date": "",
            "start_date": 20090101,
            "end_date": "20200101",
            "period": "",
            "report_type": "",
            "comp_type": "",
            "end_type": 4,
            "limit": "",
            "offset": ""
        }, fields=[
            "total_assets",
            "ann_date"
        ])
        for index, row in df.iterrows():
            data = {
                'time':row['ann_date'][:4],
                'assets':row['total_assets'],
                'ts_code':stock['ts_code'][:6]
            }
            create_one(data)


