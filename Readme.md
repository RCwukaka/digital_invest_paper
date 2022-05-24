Folder contains:
* datasource
* sql
* experiment_data

datasource: data from CSMAR et al. These data have not been processed.

sql : create Table and insert vaild data in Mysql.

experiment_data: These data are processed by Python. 


Steps:

Firstly, You should create tables in MySQL.

| Table.name | Table.introduction |
| --- | --- |
| Table.adminer_edu | Record the average educational background of listed companies adminer by year|
| Table.adminer_list | Record the educational background of each listed companies adminer |
| Table.announcements_data_analyze  | Record the keyword statistics results of each annual report by year|
| Table.announcements_list | Record the download_url of each annual report |
| Table.student | Record number of science and engineering graduates |
| Table.assets_list | Record the assets of listed company by year |
| Table.economy_index | Record market index statistics by year |
| Table.education | Regional education level statistics |
| Table.digital_invest | Record expenditure on software, etc in intangible assets |
| Table.PPE_TA |  Record PPE_TA |
| Table.roa | Record roa |
| Table.stock_iv | Record IV control variable |
| Table.stock_list | Listed company info |
| Table.tuobinq_analyzed | The tuobinq of listed company by year |

Extract the files in datasource folder, then find the corresponding Python file, According to your own situation, change the file path to the same as that in the Python program.

run Python program, then you can get experiment data in Mysql.

Also, you can insert experiment data in Mysql by run tushare_*.sql in sql folder without run Python.

Secondly, Stata analyze data is integrated in experiment_data/data.xslx. or you can get by run sql in sql/data_analyze.sql

In the end, import data in Stata, run stata/paper.do, you can get the experiment result.