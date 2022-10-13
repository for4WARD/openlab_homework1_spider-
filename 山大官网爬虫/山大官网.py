# _*_ coding: utf-8 _*_
# @Time : 2022/10/13 21:39
# @Author: 左景萱
# @File: 山大官网
# @Project: 山大官网
import urllib.parse
import urllib.request
import requests
import re
import xlsxwriter as xw
url='https://www.bkjx.sdu.edu.cn/sanji_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1010'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }
response = requests.get(url=url, headers=headers)
html = response.text



# 以下list有404，需要切片

url_list_suffix=re.findall('<a href="(.*?)" target', html)
url_list_prefix=['https://www.bkjx.sdu.edu.cn/']*len(url_list_suffix)
url_list=[url_list_prefix[i]+url_list_suffix[i] for i in range(len(url_list_suffix))]
# 以下为正确数据
title_list =re.findall('style="">(.*?)</a>', html)
time_list=re.findall('<div style="float:right;">(.*?)</div>', html)
url_list=url_list[:len(time_list)]
#至此数据收集完成
def xw_toExcel(data1,data2, data3,  fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['标题', 'url', '时间']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data1)):
        insertData = [data1[j], data2[j], data3[j]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表



# 开始爬
fileName='山大官网消息.xlsx'
xw_toExcel(title_list,url_list, time_list, fileName)




































