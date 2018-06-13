# -*- coding:gbk -*-
__author__ = 'youjia'
__date__ = '2018/5/30 16:33'

import urllib.request
import re


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('gbk', 'ignore')


def getList(html):
    reg = '<div class="box_con">(.*?)</div>'
    response = re.compile(reg, re.S)
    href = re.findall(response, html)
    # print(href)
    reg2 = '<dd><a href="(.*?)">(.*?)</a></dd>'
    res = re.compile(reg2, re.S)
    url = re.findall(res, href[1])
    return url


def content(html):
    reg = '<div id="content">(.*?)</div>'
    res = re.compile(reg, re.S)
    con = re.findall(res, html)
    return con


def bookname(html):
    reg = '<h1>(.*?)</h1>'
    name = re.compile(reg, re.S)
    b = re.findall(name, html)
    return b


if __name__ == "__main__":
    url = 'http://www.biquge.com.tw/3_3987/'
    html = getHtml(url)
    book = bookname(html)
    url_list = getList(html)
    for url, text in url_list:
        path = 'E:\\PyCharmp\\PycharmProjects\\����\\���漰�㷨\\image\\С˵\\'+book[0]+'.txt'
        # print(url, text)
        url = 'http://www.biquge.com.tw'+str(url)
        html2 = getHtml(url)
        txt = content(html2)
        with open(path, 'a+', encoding="gbk") as f:
            contents = txt[0]
            show1 = contents.replace('&nbsp;', ' ')
            show2 = '\n\n\n\n' + text + '\n\n\n\n' + show1.replace('<br />', ' ')
            f.write(show2)
            print(text+' ץȡ���...')


# https://weibo.com/2260792945/profile?rightmod=1&wvr=6&mod=personnumber
# 'http://www.biquge.com.tw/1_1872/'  # �䶯Ǭ��
# 'http://www.biquge.com.tw/1_1999/'  # ���Ʋ��
# 'http://www.biquge.com.tw/3_3987/'  # �۰�
# 'http://www.biquge.com.tw/0_83/'    # ����
# 'http://www.biquge.com.tw/16_16288/'# ���޴�½III������˵
