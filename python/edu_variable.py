# coding=gbk
from pymysql_comm import UsingMysql
import stock_list


def select_by_tscode(ts_code):
    with UsingMysql(log_time=True) as um:
        sql = "SELECT * FROM adminer_list s where ts_code = %s"
        params = (ts_code)
        um.cursor.execute(sql, params)
        return um.cursor.fetchall()


def create_one(data):
    with UsingMysql(log_time=True) as um:
        try:
            sql = "insert into adminer_edu(ts_code,edu,time) " + \
                  "values(%s,%s,%s)"
            params = (data['ts_code'], data['edu'], data['time'])
            um.cursor.execute(sql, params)
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    stocks = stock_list.select_all()
    for stock in stocks:
        adminerlist = select_by_tscode(stock['ts_code'])
        var2009, var2010, var2011, var2012, var2013, var2014, var2015, var2016, var2017, var2018, var2019, var2020 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        count2009, count2010, count2011, count2012, count2013, count2014, count2015, count2016, count2017, count2018, count2019, count2020 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        for adminers in adminerlist:
            if adminers['begin_date'] is None:
                begindate = 2009
            else:
                begindate = int(adminers['begin_date'][:4])
            if adminers['end_date'] is None:
                enddate = 2020
            else:
                enddate = int(adminers['end_date'][:4])
            if begindate <= 2009 and enddate >= 2009:
                var2009 = var2009 + 1
                count2009 = count2009 + int(adminers['edu'])
            elif begindate <= 2010 and enddate >= 2010:
                var2010 = var2010 + 1
                count2010 = count2010 + int(adminers['edu'])
            elif begindate <= 2011 and enddate >= 2011:
                var2011 = var2011 + 1
                count2011 = count2011 + int(adminers['edu'])
            elif begindate <= 2012 and enddate >= 2012:
                var2012 = var2012 + 1
                count2012 = count2012 + int(adminers['edu'])
            elif begindate <= 2013 and enddate >= 2013:
                var2013 = var2013 + 1
                count2013 = count2013 + int(adminers['edu'])
            elif begindate <= 2014 and enddate >= 2014:
                var2014 = var2014 + 1
                count2014 = count2014 + int(adminers['edu'])
            elif begindate <= 2015 and enddate >= 2015:
                var2015 = var2015 + 1
                count2015 = count2015 + int(adminers['edu'])
            elif begindate <= 2016 and enddate >= 2016:
                var2016 = var2016 + 1
                count2016 = count2016 + int(adminers['edu'])
            elif begindate <= 2017 and enddate >= 2017:
                var2017 = var2017 + 1
                count2017 = count2017 + int(adminers['edu'])
            elif begindate <= 2018 and enddate >= 2018:
                var2018 = var2018 + 1
                count2018 = count2018 + int(adminers['edu'])
            elif begindate <= 2019 and enddate >= 2019:
                var2019 = var2019 + 1
                count2019 = count2019 + int(adminers['edu'])
            else:
                var2020 = var2020 + 1
                count2020 = count2020 + int(adminers['edu'])
        if var2009 != 0:
            enu2009 = count2009 / var2009
        else:
            enu2009 = 0
        if var2010 != 0:
            enu2010 = count2010 / var2010
        else:
            enu2010 = 0
        if enu2010 == 0:
            enu2010 = enu2009
        if var2011 != 0:
            enu2011 = count2011 / var2011
        else:
            enu2011 = 0
        if enu2011 == 0:
            enu2011 = enu2010
        if var2012 != 0:
            enu2012 = count2012 / var2012
        else:
            enu2012 = 0
        if enu2012 == 0:
            enu2012 = enu2011
        if var2013 != 0:
            enu2013 = count2013 / var2013
        else:
            enu2013 = 0
        if enu2013 == 0:
            enu2013 = enu2012
        if var2014 != 0:
            enu2014 = count2014 / var2014
        else:
            enu2014 = 0
        if enu2014 == 0:
            enu2014 = enu2013
        if var2015 != 0:
            enu2015 = count2015 / var2015
        else:
            enu2015 = 0
        if enu2015 == 0:
            enu2015 = enu2014
        if var2016 != 0:
            enu2016 = count2016 / var2016
        else:
            enu2016 = 0
        if enu2016 == 0:
            enu2016 = enu2015
        if var2017 != 0:
            enu2017 = count2017 / var2017
        else:
            enu2017 = 0
        if enu2017 == 0:
            enu2017 = enu2016
        if var2018 != 0:
            enu2018 = count2018 / var2018
        else:
            enu2018 = 0
        if enu2018 == 0:
            enu2018 = enu2017
        if var2019 != 0:
            enu2019 = count2019 / var2019
        else:
            enu2019 = 0
        if enu2019 == 0:
            enu2019 = enu2018
        if var2020 != 0:
            enu2020 = count2020 / var2020
        else:
            enu2020 = 0
        if enu2020 == 0:
            enu2020 = enu2019
        create_one({"ts_code": stock['ts_code'], "time": "2009", "edu": enu2009})
        create_one({"ts_code": stock['ts_code'], "time": "2010", "edu": enu2010})
        create_one({"ts_code": stock['ts_code'], "time": "2011", "edu": enu2011})
        create_one({"ts_code": stock['ts_code'], "time": "2012", "edu": enu2012})
        create_one({"ts_code": stock['ts_code'], "time": "2013", "edu": enu2013})
        create_one({"ts_code": stock['ts_code'], "time": "2014", "edu": enu2014})
        create_one({"ts_code": stock['ts_code'], "time": "2015", "edu": enu2015})
        create_one({"ts_code": stock['ts_code'], "time": "2016", "edu": enu2016})
        create_one({"ts_code": stock['ts_code'], "time": "2017", "edu": enu2017})
        create_one({"ts_code": stock['ts_code'], "time": "2018", "edu": enu2018})
        create_one({"ts_code": stock['ts_code'], "time": "2019", "edu": enu2019})
        create_one({"ts_code": stock['ts_code'], "time": "2020", "edu": enu2020})
