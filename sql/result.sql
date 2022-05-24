*整合所有数据
SELECT
		*
FROM
    (SELECT
        t.ts_code,
            s.area,
            e.education_val,
            ei.economy_val,
            a.tuobinq,
            s.industry,
            al.assets,
            t.digitalInvest digitalInvest,
            t.time,
            t.time-s.list_date live_year,
            ae.edu,
            ifnull(oa.ppe_ta,1) PPE_TA,
            ra.roa_val roa,
            si.iv iv,
            v.bigdata
    FROM
	(SELECT
        time, SUM(money) digitalInvest, ts_code
    FROM
        tushare.digital_invest
    GROUP BY time , ts_code) t
    left join
    	(SELECT
        year time,
            ts_code,
            SUM(bigdata_num) + SUM(data_warehouse) + SUM(cloud_computing) + SUM(information_assets) + SUM(digitization) AS bigdata
    FROM
        announcements_data_analyze group by year,ts_code) v on v.ts_code = t.ts_code AND v.time = t.time
    LEFT JOIN stock_list s ON t.ts_code = s.symbol
    LEFT JOIN tuobinq_analyzed a ON a.ts_code = s.symbol AND a.time = t.time
    LEFT JOIN education e ON e.time = t.time AND e.province = s.area
    left join roa ra on ra.ts_code = t.ts_code and ra.time=t.time
    left join assets_list al on al.ts_code=s.symbol and al.time=t.time
    left join adminer_edu ae on ae.ts_code = s.ts_code and ae.time=t.time
    left join PPE_TA oa on oa.ts_code = t.ts_code and oa.time=t.time
    left join stock_iv si on si.ts_code = t.ts_code and si.time=t.time
    LEFT JOIN economy_index ei ON ei.time = t.time
        AND ei.province = s.area) rrr where rrr.industry not in( '软件服务') and rrr.tuobinq is not null  and rrr.assets is not null and rrr.roa is not null
        and rrr.ts_code in
        (select sfs.ts_code from (SELECT sds.time,sds.ts_code FROM tushare.digital_invest sds group by sds.ts_code,sds.time having sum(money)>50000) sfs group by sfs.ts_code having count(1)>4)
        order by ts_code,time;

*关键字按年汇总
select sum(t.num)/count(1),t.year from (SELECT
    (case
    when num is null then 0
    when num>50 then 50
    else num end) as num,ts_code,year
FROM
    (SELECT
        t.bigdata_num + t.data_warehouse + t.cloud_computing + t.information_assets + t.digitization AS num,t.ts_code,year
    FROM
        tushare.announcements_data_analyze t LEFT JOIN stock_list s ON s.symbol = t.ts_code
		where t.ts_code not in (select symbol from stock_list where name like '%ST%' and industry = '软件服务')) s) t group by t.year;

*出现关键字的公司数量
SELECT
    count(1),year
FROM
    tushare.announcements_data_analyze t
LEFT JOIN stock_list s ON s.symbol = t.ts_code
where t.ts_code not in (select symbol from stock_list where name like '%ST%' or industry = '软件服务')
group by year;

*计算关键字年报出现频率
select count(1),year from (SELECT
    t.bigdata_num + t.data_warehouse + t.cloud_computing + t.information_assets + t.digitization AS num,
    t.ts_code,
    year
FROM
    tushare.announcements_data_analyze t
        LEFT JOIN
    stock_list s ON s.symbol = t.ts_code
WHERE
    t.ts_code NOT IN (SELECT
            symbol
        FROM
            stock_list
        WHERE
            name LIKE '%ST%' AND industry = '软件服务')) s where s.num>0 group by s.year;
