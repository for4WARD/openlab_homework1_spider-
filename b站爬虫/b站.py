# _*_ coding: utf-8 _*_
# @Time : 2022/10/13 22:45
# @Author: 左景萱
# @File: b站
# @Project: b站
import requests
import json
import urllib.parse
import urllib.request
import xlsxwriter as xw


# PART1:获取相同关注的uid

# 先找出所提供的两人uid所的关注列表
def uid_getter(uid, page, uid_list):
    # url = 'https://api.bilibili.com/x/relation/followings?vmid=418344235&pn=2&ps=20&order=desc&order_type=attention&jsonp=jsonp&callback=__jp6'  # jp后面的数字没关系
    url1 = 'https://api.bilibili.com/x/relation/followings?'
    url_pluser = {
        'vmid': uid,
        'pn': page
    }
    url2 = '&ps=20&order=desc&order_type=attention&jsonp=jsonp&callback=__jp6'
    url_pluser = urllib.parse.urlencode(url_pluser)
    url = url1 + url_pluser + url2
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'cookie': 'buvid3=F75DB8A1-6D70-D06A-82A2-80DF64630B7510940infoc; b_nut=1665710210; i-wanna-go-back=-1; _uuid=9E6195A6-10DE6-34B9-96D7-DB10C86A1B9B811311infoc; buvid4=8EFACE72-3F03-8967-7B26-6161A5345A4211683-022101409-jFX7KwtKp+SnsxBGGRCO8w%3D%3D; fingerprint=c22d88faacc113b049f4f548d9c9a017; buvid_fp_plain=undefined; SESSDATA=7ed783f4%2C1681262256%2Cec93e%2Aa1; bili_jct=0d1eb454ba8d2b294946bd419c910c47; DedeUserID=418344235; DedeUserID__ckMd5=3d22e3aad639c1d3; sid=7fqa9896; buvid_fp=c22d88faacc113b049f4f548d9c9a017; b_ut=5; b_lsid=1F8191089_183D5A0676B; bsource=search_google; bp_video_offset_418344235=716818359574855700; PVID=2; innersign=1; CURRENT_FNVAL=4048; rpdid=|(J~RYlm|J|~0JuYYl~JYRkR'
        , 'referer': 'https://space.bilibili.com/418344235/fans/follow'
    }
    response = requests.get(url=url, headers=headers)
    html = response.text
    html_1 = html[6:len(html) - 1]  # 获取json字符串

    if html_1:
        html_ok = json.loads(html_1)  # 转化为dict
        # 找出list列表
        data = html_ok['data']
        data = data['list']
        for i in range(len(data)):
            uid_list.append(data[i]['mid'])

        return uid_list
    else:
        return uid_list


# PART2:由uid推出对应的信息
def follwer_getter(uid):
    # url = 'https://api.bilibili.com/x/relation/stat?vmid=946974&jsonp=jsonp'
    url1 = 'https://api.bilibili.com/x/relation/stat?'
    url_pluser = {
        'vmid': uid,
        'jsonp': 'jsonp'

    }

    url_pluser = urllib.parse.urlencode(url_pluser)
    url = url1 + url_pluser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'cookie': 'buvid3=F75DB8A1-6D70-D06A-82A2-80DF64630B7510940infoc; b_nut=1665710210; i-wanna-go-back=-1; _uuid=9E6195A6-10DE6-34B9-96D7-DB10C86A1B9B811311infoc; buvid4=8EFACE72-3F03-8967-7B26-6161A5345A4211683-022101409-jFX7KwtKp+SnsxBGGRCO8w%3D%3D; fingerprint=c22d88faacc113b049f4f548d9c9a017; buvid_fp_plain=undefined; SESSDATA=7ed783f4%2C1681262256%2Cec93e%2Aa1; bili_jct=0d1eb454ba8d2b294946bd419c910c47; DedeUserID=418344235; DedeUserID__ckMd5=3d22e3aad639c1d3; sid=7fqa9896; buvid_fp=c22d88faacc113b049f4f548d9c9a017; b_ut=5; b_lsid=1F8191089_183D5A0676B; bsource=search_google; bp_video_offset_418344235=716818359574855700; PVID=2; innersign=1; CURRENT_FNVAL=4048; rpdid=|(J~RYlm|J|~0JuYYl~JYRkR'
        , 'referer': 'https://space.bilibili.com/418344235/fans/follow'
    }
    response = requests.get(url=url, headers=headers)
    html = response.text  # 得到json字符串
    html = json.loads(html)  # 得到dict
    num_of_follower = html['data']['follower']
    return num_of_follower


def name_getter(uid):
    # url = 'https://api.bilibili.com/x/space/acc/info?mid=946974&token=&platform=web&jsonp=jsonp'
    url1 = 'https://api.bilibili.com/x/space/acc/info?'
    url_pluser = {
        'mid': uid,
        'token': ''
    }
    url2 = '&platform=web&jsonp=jsonp'
    url_pluser = urllib.parse.urlencode(url_pluser)
    url = url1 + url_pluser + url2
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'cookie': 'buvid3 = F75DB8A1 - 6D70 - D06A - 82A2 - 80DF64630B7510940infoc;b_nut = 1665710210;i - wanna - go - back = -1;_uuid = 9E6195A6 - 10DE6 - 34B9 - 96D7 - DB10C86A1B9B811311infoc;buvid4 = 8EFACE72 - 3F03 - 8967 - 7B26 - 6161A5345A4211683 - 022101409 - jFX7KwtKp + SnsxBGGRCO8w % 3D % 3D;fingerprint = c22d88faacc113b049f4f548d9c9a017;buvid_fp_plain = undefined;SESSDATA = 7ed783f4 % 2C1681262256 % 2Cec93e % 2Aa1;bili_jct = 0d1eb454ba8d2b294946bd419c910c47;DedeUserID = 418344235;DedeUserID__ckMd5 = 3d22e3aad639c1d3;sid = 7 fqa9896; buvid_fp = c22d88faacc113b049f4f548d9c9a017; b_ut = 5; bsource = search_google; rpdid = | (J ~RYlm | J | ~0J uYYl~JYRkR; bp_video_offset_418344235=716827877216092161; fingerprint3=8f1a47c5e1ca3909eb5f8eb9f10a1383; CURRENT_FNVAL=4048; PVID=5; b_lsid=E10AB1043D_183D5F33496; innersign=1',
        'referer': 'https://space.bilibili.com/946974'
    }
    response = requests.get(url=url, headers=headers)
    html = response.text  # 得到json字符串
    html = json.loads(html)  # 得到dict
    name = html['data']['name']
    return name


def level_getter(uid):
    # url = 'https://api.bilibili.com/x/space/acc/info?mid=946974&token=&platform=web&jsonp=jsonp'
    url1 = 'https://api.bilibili.com/x/space/acc/info?'
    url_pluser = {
        'mid': uid,
        'token': ''
    }
    url2 = '&platform=web&jsonp=jsonp'
    url_pluser = urllib.parse.urlencode(url_pluser)
    url = url1 + url_pluser + url2
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'cookie': 'buvid3 = F75DB8A1 - 6D70 - D06A - 82A2 - 80DF64630B7510940infoc;b_nut = 1665710210;i - wanna - go - back = -1;_uuid = 9E6195A6 - 10DE6 - 34B9 - 96D7 - DB10C86A1B9B811311infoc;buvid4 = 8EFACE72 - 3F03 - 8967 - 7B26 - 6161A5345A4211683 - 022101409 - jFX7KwtKp + SnsxBGGRCO8w % 3D % 3D;fingerprint = c22d88faacc113b049f4f548d9c9a017;buvid_fp_plain = undefined;SESSDATA = 7ed783f4 % 2C1681262256 % 2Cec93e % 2Aa1;bili_jct = 0d1eb454ba8d2b294946bd419c910c47;DedeUserID = 418344235;DedeUserID__ckMd5 = 3d22e3aad639c1d3;sid = 7 fqa9896; buvid_fp = c22d88faacc113b049f4f548d9c9a017; b_ut = 5; bsource = search_google; rpdid = | (J ~RYlm | J | ~0J uYYl~JYRkR; bp_video_offset_418344235=716827877216092161; fingerprint3=8f1a47c5e1ca3909eb5f8eb9f10a1383; CURRENT_FNVAL=4048; PVID=5; b_lsid=E10AB1043D_183D5F33496; innersign=1',
        'referer': 'https://space.bilibili.com/946974'
    }
    response = requests.get(url=url, headers=headers)
    html = response.text  # 得到json字符串
    html = json.loads(html)  # 得到dict
    level = html['data']['level']
    return level


# PAR3:写入表格
def xw_toExcel(i, uid_final_list):  # xlsxwriter库储存数据到excel
    # 获取uid_list
    # 从第二行开始写入数据
    for j in range(len(uid_final_list)):
        uid = uid_final_list[j]
        name = name_getter(uid)
        level = level_getter(uid)
        follower = follwer_getter(uid)
        insertData = [uid, name, level, follower]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i+=1


# PART4:主程序入口
if __name__ == '__main__':
    uid1 = int(input('请输入第一个对象的uid:'))
    page1 = int(input('请输入希望寻找他（她，它）的关注页面数量（每页20人，且非自己的情况下不输入超过5）'))
    uid2 = int(input('请输入第二个对象的uid:'))
    page2 = int(input('请输入希望寻找他（她，它）的关注页面数量（每页20人，且非自己的情况下输入不大于5）'))
    # 创建空背包
    uid_list1 = []
    uid_list2 = []
    uid_final_list = []
    # 对于第一个uid
    try:
        for page in range(page1):
            uid_list_final1 = uid_getter(uid1, page, uid_list1)
        if len(uid_list_final1) < 20:
            print('一号用户： ' + str(uid1) + ' 不常用b站')

        # 对于第二个uid
        for page in range(page2):
            uid_list_final2 = uid_getter(uid2, page, uid_list2)
        if len(uid_list_final1) < 20:
            print('二号用户： ' + str(uid2) + ' 不常用b站')

        # 获得了共同关注up的uid
        for i in range(len(uid_list_final1)):
            if uid_list_final1[i] in uid_list_final2:
                uid_final_list.append(uid_list_final1[i])

        # 开始写入吧！！!
        fileName = 'b站共同关注列表.xlsx'
        workbook = xw.Workbook(fileName)  # 创建工作簿
        worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
        worksheet1.activate()  # 激活表
        title = ['UID', '用户昵称', 'b站等级', '粉丝数']  # 设置表头
        worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
        i = 2
        xw_toExcel(i, uid_final_list)
        workbook.close()
    except KeyError:
        print('\n系统正在升级（bushi \n有个用户设置了关注隐私了捏！')