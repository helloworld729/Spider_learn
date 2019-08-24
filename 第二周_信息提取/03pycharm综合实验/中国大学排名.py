import requests
from bs4 import BeautifulSoup
import bs4


def get_html_text(url):
    html = ""
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
    except:
        print('Error')
    return html


def get_information(ulist, html):
    """
    get important information and add them to a list[rank, name, score]
    :param ulist: 2_demension list
    :param html:  information sourcr
    :return: html
    """
    university_soup = BeautifulSoup(html, 'html.parser')
    for university in university_soup.find('tbody').children:
        if isinstance(university, bs4.element.Tag):
            infos = university.find_all('td')
            ulist.append([infos[0].string, infos[1].string, infos[2].string, infos[3].string])
    return ulist


def print_information(ulist, num):
    """
    :param ulist: university 2—demension list
    :param num:
    :return:
    """
    print("{0:{4}^10}\t{1:{4}^16}\t{2:{4}^510}\t{3:{4}^5}".format('名次', '校名', '地区', '分数', chr(12288)))
    for university in ulist[:num]:
        print("{0:{4}^10}\t{1:{4}^16}\t{2:{4}^5}\t{3:{4}^5}".format(university[0], university[1], university[2], university[3], chr(12288)))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
    html = get_html_text(url)
    get_information(uinfo, html)
    print_information(uinfo, 15)
main()



# 老师的代码侧重对标签用find方法检索， 我侧重用方法遍历。




# html = get_html_text('http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html')
# soup = BeautifulSoup(html, 'html.parser')
# ufather = soup.find(string='清华大学').parent.parent.parent.parent
# uinfos = []
#
# for university in ufather.contents:
#     if university != '\n':  # 学校的最外层标签,考虑换行和注释
#         info=[]
#         try:
#             for child in university.children:
#                 if child != '\n' and len(info)<4:
#                     info.append(child.string)
# #               print(info)
#             uinfos.append(info)
#         except:pass
# for university in uinfos:
#     print(university)