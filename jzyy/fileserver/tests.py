from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.template import RequestContext
from django.urls import reverse
from django.utils.http import urlquote
import os,stat,shutil,sys,win32com.client
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import get_user
import pythoncom
from pydocx import PyDocX
from PyPDF2 import PdfFileReader, PdfFileWriter
import time,xlrd,pymysql
from django.contrib import messages

db = pymysql.connect("127.0.0.1", "root", "password", "jzyy")

 
def open_excel():
    try:
        book = xlrd.open_workbook(r"D:\python\jzyy\updog\20201015.xlsx")  #文件名，把文件与py文件放在同一目录下
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("Sheet0")   #execl里面的worksheet1
        return sheet
    except:
        print("locate worksheet in excel failed!")
 
 
def insert_deta():
    sheet = open_excel()
    cursor = db.cursor()
    row_num = sheet.nrows
    for i in range(1, row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
        row_data = sheet.row_values(i)
        value = (row_data[1],row_data[0],row_data[2],row_data[3])
        print(i)
        sql = "INSERT INTO fileserver_xqtj(id,work_id,name,tj_path)VALUES(%s,%s,%s,%s)"
        cursor.execute(sql, value)  # 执行sql语句
        db.commit()
    cursor.close()  # 关闭连接
 
 
open_excel()
insert_deta()