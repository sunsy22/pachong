# -*- coding: utf-8 -*-
import os, re, threading

import requests
from bs4 import BeautifulSoup
import time
class saveAsMD():
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
    def get_article_link(self):
        url_link = []
        for i in range(20, 30):
            url = "http://chuansong.me/account/dujinyong6?start=" + str(i*12)
            datas = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(datas.text, "html.parser")
            all_a = soup.find_all("a", {"class", "question_link"})
            patter = re.compile("href=\"(.+?)\"")
            for i in all_a:
                result_i = patter.search(repr(i))
                if result_i:
                    for j in result_i.groups(1):
                        url_link.append(j)
            time.sleep(3)
        return url_link
    def saveAsMd(self, links):
        pathName = []
        for i in links:
            mdBefore = []
            url = "http://chuansong.me"+i
            response = requests.get(url, header=self.headers)
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.soup.find('title').getText().split('_')[0]
            title1 = 'c_start' + title.strip()
            content = {'tag': 'title', 'content': title1}
            mdBefore.append(content)
            imgTitle = ''
            media = soup.find('div', id='media')
            if url == "http://chuansong.me/n/1596902743617":
                pimg = soup.findAll('p')
                imgTitle = pimg[1].img['src']

            elif media == None:
                imgTITLE = "http://read.html5.qq.com/image?src=forum&q=5&r=0&imgflag=7&imageUrl=http://" \
                           "mmbiz.qpic.cn/mmbiz_jpg/EC7unEiaL8xrnFiaicD6NBibS1mialXtnScibg315ygyyRucV12VcDqKtyaPRFHM1XEe" \
                           "AiceGxH2Igcl7ot4qB2duU2Ig/0?wx_fmt=jpeg"

            else:
                imgTITLE = media.img['src']
            content = {'tag': 'img', 'content': imgTITLE}
            mdBefore.append(content)
            ps = soup.findAll('p')
            for p in ps:
                img = p.img
                if img != None:
                    content = {'tag': 'img', 'content': img['src']}
                    mdBefore.append(content)

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
                                    mdBefore.append(content)
                else:
                    content = {'tag': 'text1', 'content': p.getText()}
                    mdBefore.append(content)

            with open('./book/' + title.strip() + '.md', 'wb') as f:
                pathTitle = './book/' + title.strip()
                path = './book/' + title.strip() + '.md'
                pathALL = {
                    'title': pathTitle,
                    'path': path
                }
                pathName.append(pathALL)
                # pathName.append("./book/" + title.strip() + ".md")
                for i in mdBefore:
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

            time.sleep(3)

if __name__ == "__main()__":
    saveAsMD = saveAsMD()
    links = saveAsMD.get_article_link()
    md = saveAsMD.saveAsMd(links)




