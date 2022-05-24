# coding=gbk
import os
import logging
import pdfplumber
import re
from .. import pymysql_comm


def exit(ts_code,ann_date,ann_type):
    with pymysql_comm.UsingMysql(log_time=True) as um:
        sql = "select * from announcements_data_analyze where ts_code = %s and ann_date = %s and ann_type = %s"
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
            sql = "insert into announcements_data_analyze(ts_code,bigdata_num,data_warehouse,cloud_computing,information_assets,digitization,ann_date,year) " + \
                  "values(%s,%s,%s,%s,%s,%s,%s,%s)"
            params = (data['ts_code'],data['bigdata_num'],data['data_warehouse'],data['cloud_computing'],data['information_assets'],data['digitization'],data['ann_date'],data['year'])
            um.cursor.execute(sql, params)
            print(data['ts_code'] + "==" + data['year'] + "==" + str(data['bigdata_num']) + "/" + str(data['data_warehouse']) + "/" +str(data['cloud_computing']) + "/" + str(data['information_assets']) + "/" + str(data['digitization']))
        except BaseException as e:
            print(e)


def select_by_tscodeandyear(ts_code,year):
    with pymysql_comm.UsingMysql(log_time=True) as um:
        sql = "SELECT * FROM announcements_data_analyze s where ts_code = %s and s.year = %s"
        params = (ts_code,year)
        um.cursor.execute(sql,params)
        return um.cursor.fetchall()

def update_by_pk(data):
    with pymysql_comm.UsingMysql(log_time=True) as um:
        sql = "update announcements_data_analyze s set bigdata_num = %s , data_warehouse = %s , cloud_computing = %s , information_assets = %s , digitization = %s where s.ts_code = %s and s.year = %s"
        params = (data['bigdata_num'],data['data_warehouse'],data['cloud_computing'],data['information_assets'],data['digitization'],data['ts_code'],data['year'])
        um.cursor.execute(sql, params)

def is_chinese(uchar):
    if uchar >= '\u4e00' and uchar <= '\u9fa5':
        return True
    else:
        return False

if __name__ == '__main__':
    log_name = "log"
    logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        filename="./" + log_name)
    logger = logging.getLogger(__name__)
    for filepath, dirnames, filenames in os.walk(r'./announcement/'):
        for filename in filenames:
            stockcode = filename[:6]
            s=filename.split("_")[1]
            year = re.sub("\D","",s)

            bigdata_num = 0
            data_warehouse = 0
            information_assets = 0
            cloud_computing = 0
            digitization = 0
            try:
                file_path = "./announcement/" + filename
                with pdfplumber.open('./announcement/' + filename) as pdf:
                    for page in pdf.pages:
                        content = page.extract_text()
                        if (is_chinese(content)):
                            bigdata_num += content.count("大数据")
                            data_warehouse += content.count("数据仓库")
                            cloud_computing += content.count("云计算")
                            information_assets += content.count("信息资产")
                            digitization += content.count("数字化")

                    data={"ts_code":stockcode,"bigdata_num":bigdata_num,"data_warehouse":data_warehouse,"cloud_computing":cloud_computing,"information_assets":information_assets,
                          "digitization":digitization,"ann_date":year,"year":year}
                    logger.info(f"当前正在插入处理的是：{data['ts_code']},当前的年份是：{data['year']},当前的pdf是：{data['ann_date']}")
                    create_one(data)
            except BaseException as e:
                continue