import requests
from bs4 import BeautifulSoup
import re
import traceback


def get_html_text(url, code='utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


def get_writer_list(url, writer_list):
    html = get_html_text(url)
    soup = BeautifulSoup(html, 'html.parser')
    href_set = soup.find_all('a')

    names = []
    for href in href_set:
        try:
            if href.attrs['title'] == '作品数量':
                link = href.attrs['href']
                writer_list.append(re.findall(r'XianDaiAuthor[A-Za-z0-9]{8}-[A-Za-z0-9]{4}-'
                                              r'[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{12}', link)[0])
                names.append(href.string.split()[-2])
        except:
            pass
    return names


def get_writer_works(writer_url,work_list):
    boot_url = 'http://www.chinapoesy.com/'
    dest_url = boot_url + writer_url + '.html'
    html = get_html_text(dest_url)
    soup = BeautifulSoup(html, 'html.parser')

    href_set = soup.find_all('a', attrs={'title': '人气指数'})
    for href in href_set:
        try:
            link = re.findall(r'XianDai[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}', href.attrs['href'])[0]
            work_list.append(link)
        except:pass
    return ""


def get_work_content(url,file_path):
    boot_url = 'http://www.chinapoesy.com/'
    dest_url = boot_url + url + ',html'
    html = requests.get(dest_url).text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find_all('div', attrs={"class": "HeightBorderCenter", "style": "text-align:left; margin-left:60px;"})
    result = re.findall(r'[\u4e00-\u9fa5]+', content[0].text)
    try:
        begin = result[0]
        for sen in result[1:]:
            begin += ',' + sen
        article = begin + '。\n'

        with open(file_path, 'a') as f:  # 追加方式
            f.write(article)
    except:pass






def main():
    writers_url = 'http://www.chinapoesy.com/XianDaiAuthorList_1.html'
    file_path = 'poems.txt'
    # 获取诗人链接列表
    writer_list = []
    get_writer_list(writers_url, writer_list)
    # print(writer_list)


    # 获取每个诗人的作品链接列表（传入诗人链接，返回作品链接）
    total_works = []
    count = 0
    for writer_url in writer_list:
        work_list = []
        get_writer_works(writer_url, work_list)
        total_works.extend(work_list)

        count += 1
        print("\r爬取诗人作品链接进度: {:.2f}%".format(100 * count/len(writer_list)), end="")


    step = 0
    for work_url in total_works:
        get_work_content(work_url,file_path)
        step += 1
        print("\r诗人作品写入磁盘进度: {:.2f}%".format(step/len(total_works)), end="")

main()