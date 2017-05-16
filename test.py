# -*- coding: utf-8 -*-
import os, re, threading

import requests
from bs4 import BeautifulSoup
import time

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
url_link = []
def get_article_link():
    for i in range(0, 5):
        url = "http://chuansong.me/account/dujinyong6?start=" + str(i * 12)
        datas = requests.get(url, headers=headers)
        soup = BeautifulSoup(datas.text, "html.parser")
        all_a = soup.find_all("a", {"class", "question_link"})
        patter = re.compile("href=\"(.+?)\"")
        for i in all_a:
            result_i = patter.search(repr(i))
            if result_i:
                for j in result_i.groups(1):
                    url_link.append(j)

        time.sleep(3)

    # import pdb
    # pdb.set_trace()
# for i in range(0, 30):
#     url = "http://chuansong.me/account/dujinyong6?start=" + str(i*12)
#     datas = requests.get(url, headers=headers)
#     soup = BeautifulSoup(datas.text, "html.parser")
#     get_article_link(soup)
#     time.sleep(3)
get_article_link()
print(len(url_link))
time.sleep(10)
for i in url_link:
    print(i)
def saveAsMD():
    pathName = []
    for i in url_link:
        papers = []
        imgTITLE = ''
        url = "http://chuansong.me"+i
        print(url)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup)
        title = title = soup.find('title').getText()
        title1 = 'c_start' + title.strip()
        content = {'tag': 'title', 'content': title1}
        papers.append(content)
        print(title)
        media = soup.find('div', id='media')
        if url == "http://chuansong.me/n/1596902743617":
            pimg = soup.findAll('p')
            imgTITLE = pimg[1].img['src']
        elif media == None:
            imgTITLE = "http://read.html5.qq.com/image?src=forum&q=5&r=0&imgflag=7&imageUrl=http://" \
                       "mmbiz.qpic.cn/mmbiz_jpg/EC7unEiaL8xrnFiaicD6NBibS1mialXtnScibg315ygyyRucV12VcDqKtyaPRFHM1XEe" \
                       "AiceGxH2Igcl7ot4qB2duU2Ig/0?wx_fmt=jpeg"
        else:
            imgTITLE = media.img['src']
        content = {'tag': 'img', 'content': imgTITLE}
        papers.append(content)
        print(content)
        ps = soup.findAll('p')
        for p in ps:
            img = p.img
            if img != None:
                content = {'tag': 'img', 'content': img['src']}
                papers.append(content)

            elif p.span != None:
                spans = p.findAll('span')  # 找到所有的span标签
                for span in spans:
                    # print(span.text)
                    style = span.get('style')
                    if style != None:
                        if span.get('style').find('color') != -1:
                            if span.string != None:
                                print(span.string)
                                spanString = 'c_start' + span.string + 'c_end'
                                content = {'tag': 'text', 'content': spanString}
                                papers.append(content)
            else:
                content = {'tag': 'text1', 'content': p.getText()}
                papers.append(content)

        print(papers[1])
        # f = open(title.strip() + '.md', 'wb')

        with open('./book/'+title.strip() + '.md', 'wb') as f:
            pathTitle = './book/'+title.strip()
            path = './book/'+title.strip() + '.md'
            pathALL = {
                'title': pathTitle,
                'path': path
            }
            pathName.append(pathALL)
            # pathName.append("./book/" + title.strip() + ".md")
            for i in papers:
                print(i)
                str = ''
                if i['tag'] == 'text':
                    str = i['content'].replace('c_start', '**').replace('c_end', '**')
                elif i['tag'] == 'title':
                    str = i['content'].replace('c_start', '##')
                elif i['tag'] == 'img':
                    str = '![](%s)' % (i['content'])
                    str = '\r\n' + str + '\r\n'
                else:
                    str = i['content']
                f.write(str.encode('utf-8'))
                f.write('\r\n'.encode('utf-8'))
        time.sleep(5)
saveAsMD()
# with open("./book/SUMMARY.md", "wb") as summaryfile:
#     for i in pathALL:
#         path1 = '*' + ' ' + '[' + i['title'] + '](' + i[path] + ')'
#         summaryfile.write(path1.encode('utf-8'))
# saveAsMD()