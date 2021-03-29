# 读取excel表的内容然后写入数据库
import xlrd,pymysql
 

conn = pymysql.connect(host='127.0.0.1', user="root", password='password'
                                , database='jzyy', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
try:
    sql = "insert into jzyy.fileserver_xqtj(work_id, name, tj_path) values (%s,%s,%s)"
            #打开文件
    file = xlrd.open_workbook(r'D:\python\jzyy\tmp\07.xls')
    sheet_1 = file.sheet_by_index(0) #根据sheet页的排序选取sheet
    row_content = sheet_1.row_values(0) #获取指定行的数据，返回列表，排序自0开始
    row_number = sheet_1.nrows #获取有数据的最大行数
    for i in range(1,row_number):
        work_id = sheet_1.cell(i,1).value
        name = sheet_1.cell(i,13).value
        tj_path = sheet_1.cell(i,14).value
        values = (work_id, name, tj_path)
            #执行sql语句插入数据
        cursor.execute(sql,values)
        conn.commit()
except Exception as e:
    conn.rollback()
cursor.close()
conn.close()

