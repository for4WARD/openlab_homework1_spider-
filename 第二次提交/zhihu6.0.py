# _*_ coding: utf-8 _*_
# @Time : 2022/10/13 16:09
# @Author: 左景萱
# @File: 知乎5.0
# @Project: 浅浅卷一下
import urllib.parse
import urllib.request
import requests
import json
import xlsxwriter as xw
'''xlsx无法一次写入要求的种类的数据，所以得定义两个函数完成（我超）
第二章20条
其余都是19条
超
看了一个下午
超第一页咋也变成20条了
超第二页变成17条了
'''
'''仅对当前版本有用'''



# 创建一个namehelper解决标签数量不一致的问题
def data_name_helper(data,j):
    list=[]
    data_list=data[j]['question']['topics']
    if data_list:
        for i in range(len(data_list)):
            list.append(data_list[i]['name'])
        str1 = ' '.join(list)
    else:
        str1=' '
    return str1


def data_getter(page):
    # 获取data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    if page > 1:

        url_title = 'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&'

        data = {
            'limit': 20,
            'offset': page * 20,
            'period ': 'hour'
        }
        data = urllib.parse.urlencode(data)
        url = url_title + data
    else:
        url = 'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&period=hour'
    response = requests.get(url=url, headers=headers)
    html = response.text
    html_ok = json.loads(html)  # 转化为dict
    data = html_ok['data']  # 转化为列表
    print(len(data))  # 用于找出错误，即条数的版本
    return data


def xw_toExcel(i,data):  # xlsxwriter库储存数据到excel
    # 获取data
    if True:
        # 从上一次的末尾开始写入数据
        for j in range(len(data)):
            insertData = [data_name_helper(data,j),data[j]['question']['title'],
                          data[j]['question']['url'], data[j]["reaction"]['score']]
            row = 'A' + str(i)
            worksheet1.write_row(row, insertData)
            i += 1



# 主程序入口

if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页面'))
    fileName = '知乎热榜.xlsx'
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['话题', '标题', '链接', '热力值']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头

    i=2
    for page in range(start_page, end_page + 1):
        data = data_getter(page)
        xw_toExcel(i,data)
        i = i+len(data)

    workbook.close()  # 关闭表






























