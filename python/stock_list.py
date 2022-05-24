from pymysql_comm import UsingMysql


# 新增单条记录
def create_one(data):
    with UsingMysql(log_time=True) as um:
        try:
            sql = "insert into stock_list(ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs) " + \
                  "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            params = (data['ts_code'], data['symbol'], data['name'], data['area'], data['industry'], data['fullname'],
                      data['enname'], data['market'], data['exchange'], data['curr_type'], data['list_status'],
                      data['list_date'], data['delist_date'], data['is_hs'])
            um.cursor.execute(sql, params)
        except BaseException as e:
            print(e)


def select_by_ts_code(tscode):
    with UsingMysql(log_time=True) as um:
        sql = 'select * from stock_list where ts_code = %s'
        params = (tscode)
        um.cursor.execute(sql, params)
        return um.cursor.fetchall()


def select_all():
    with UsingMysql(log_time=True) as um:
        sql = "SELECT * FROM stock_list where name not like '%ST%'"
        um.cursor.execute(sql)
        return um.cursor.fetchall()


import tushare as ts

pro = ts.pro_api('809e1cd982cabb44bcf52bb954e665438df8b1c84191e6aaf70dbf1c')

if __name__ == '__main__':
    df = pro.stock_basic(**{
        "ts_code": "",
        "name": "",
        "exchange": "",
        "market": "",
        "is_hs": "",
        "list_status": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "ts_code",
        "symbol",
        "name",
        "area",
        "industry",
        "market",
        "list_date",
        "fullname",
        "enname",
        "exchange",
        "list_status",
        "curr_type",
        "is_hs",
        "delist_date"
    ])
    for index, data in df.iterrows():
        create_one(data)
