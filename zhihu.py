# _*_ coding: utf-8 _*_
# @Time : 2022/10/12 20:32
# @Author: 左景萱
# @File: zhihu
# @Project: 浅浅卷一下

import urllib.parse
import urllib.request
import requests
import json
import xlsxwriter as xw
'''xlsx无法一次写入要求的种类的数据，所以得定义两个函数完成（我超）
第一章有19条，第二章开始20条'''





def xw_toExcel1(page):  # xlsxwriter库储存数据到excel
        # 获取data
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }
        if page > 1:

            url_title = 'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&'

            data = {
                'limit': 20,
                'offset': (page - 1) * 20,
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

        if page==1:
            i = 2  # 从上一次的末尾开始写入数据
        else:
            i = 1+(page - 1) * 20
        for j in range(10):
            insertData = [data[j]['question']['topics'][0]['name'], data[j]['question']['topics'][1]['name'],
                          data[j]['question']['topics'][2]['name'],
                          data[j]['question']['title'],
                          data[j]['question']['url'], data[j]["reaction"]['score']]
            row = 'A' + str(i)
            worksheet1.write_row(row, insertData)
            i += 1
if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页面'))
    fileName = '知乎热榜.xlsx'
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['话题1', '话题2','话题3','标题', '链接', '热力值']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    page=start_page


    xw_toExcel1(page)

    workbook.close()  # 关闭表
