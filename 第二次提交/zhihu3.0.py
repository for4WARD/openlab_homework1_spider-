# _*_ coding: utf-8 _*_
# @Time : 2022/10/12 23:49
# @Author: 左景萱
# @File: zhihu3.0
# @Project: 浅浅卷一下
import requests
import json
import re

import pandas as pd

url = 'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&limit=20&offset=40&period=hour'

headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',

}
response = requests.get(url=url, headers=headers)
html=response.text
html_ok=json.loads(html) #转化为dict
data=html_ok['data']
print(len(data))
import xlsxwriter as xw

# 接下来创建关键词字典  热点分类"name"、标题"title"、链接"url"、热力值"score"


'''def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['标题', '链接','热力值','话题性质']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据

    for j in range(3):
        insertData = [data[j]['question']['topics'][0]['name'], data[j]['question']['topics'][1]['name'], data[j]['question']['topics'][2]['name'], data[j]['question']['title'], data[j]['question']['url'], data[j]["reaction"]['score'], data[j]['question']['label']]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    for j in range(3,7):
        insertData = [data[j]['question']['topics'][0]['name'], data[j]['question']['topics'][1]['name'], data[j]['question']['topics'][2]['name'], data[j]['question']['title'], data[j]['question']['url'], data[j]["reaction"]['score'], data[j]['question']['label']]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表


print(data[0]['question']['title'])

fileName = '知乎热榜.xlsx'
xw_toExcel(data, fileName)'''


'''def create_data(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    if page>1:

        url_title = 'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&'

        data = {
            'limit':(page - 1) * 20,
            'offset':20,
            'period ':'hour'
        }
        data = urllib.parse.urlencode(data)
        url = url_title + data
    else:
        url = 'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&period=hour'
    response = requests.get(url=url, headers=headers)
    html = response.text
    html_ok = json.loads(html)  # 转化为dict
    data = html_ok['data']  # 转化为列表
    return data'''

















#
#
# print(type(data[0]))
