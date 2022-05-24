# coding=gbk
import tushare as ts
from .. import stock_list
import time
import re
from .. import pymysql_comm

def exit(ts_code,ann_date,ann_type):
    with pymysql_comm.UsingMysql(log_time=True) as um:
        sql = "select * from announcements_list where ts_code = %s and ann_date = %s and ann_type = %s"
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

    with pymysql_comm.UsingMysql(log_time=True) as um:
        try:
            sql = "insert into announcements_list(ts_code,ann_date,ann_type,title,pub_time,src_url) " + \
                  "values(%s,%s,%s,%s,%s,%s)"
            params = (data['ts_code'],data['ann_date'],data['ann_type'],data['title'],data['pub_time'],data['src_url'])
            um.cursor.execute(sql, params)
        except BaseException as e:
            print(e)


def select_by_tscode(ts_code):
    with pymysql_comm.UsingMysql(log_time=True) as um:
        sql = "SELECT * FROM announcements_list where ts_code = %s"
        params = (ts_code)
        um.cursor.execute(sql,params)
        return um.cursor.fetchall()

def select_all():
    with pymysql_comm.UsingMysql(log_time=True) as um:
        sql = "SELECT * FROM announcements_list"
        um.cursor.execute(sql)
        return um.cursor.fetchall()

def update_by_pk(ann_date,id):
    with pymysql_comm.UsingMysql(log_time=True) as um:
        sql = "update announcements_list set ts_code = %s where id = %s"
        params = (ann_date,id)
        um.cursor.execute(sql, params)

pro = ts.pro_api('809e1cd982cabb44bcf52bb954e665438df8b1c84191e6aaf70dbf1c')

date_range = ['20090101~20100101','20100101~20110101','20110101~20120101','20120101~20130101','20130101~20140101','20140101~20150101','20150101~20160101',
              '20160101~20170101','20170101~20180101','20180101~20190101','20190101~20200101']
stocks = stock_list.select_all()
for values in stocks:
    for date in date_range:
        time.sleep(0.5)
        df = pro.anns(**{
            "ts_code": values['ts_code'],
            "ann_date": "",
            "start_date": date.split("~")[0],
            "end_date": date.split("~")[1],
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "ann_date",
            "title",
            "ann_type",
            "src_url",
            "pub_time"
        ])
        for index, row in df.iterrows():
            if row['ann_type'].find("年报") != -1 and row['ann_type'].find("半年度报告") == -1 and row['title'].find("已取消") == -1 and row['title'].find("补充公告") == -1:
                anndate = re.sub("\D", "", row['title'])
                row['ann_date'] = anndate -1
                if not exit(row['ts_code'],row['ann_date'],row['ann_type']):
                    create_one(row)
