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


def get_stock_list(stoList, stock_list_url):
    """
    获取股票代码列表
    :param stoList: 存储代码的列表
    """
    html = get_html_text(stock_list_url,code='GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a_set = soup.find_all('a')  # 返回由a标签构成的resultset
    for link in a_set:
        try:
            href = link.attrs['href']
            num = re.findall(r'[s][hz]\d{6}', href)[0]
            stoList.append(num)
        except:pass


def get_stock_info(stoList, stock_info_url, file_path, num_limit= 10):
    """
    将 股票名称 与 股票代码 封装成 键值对 存储到 字典-->文件中
    :param stoList:  代码列表
    :param stock_info_url: 个股根路径
    :param file_path: 保存文件的路径
    :return:
    """
    infoDict = {}
    count = 0
    boot_url = stock_info_url

    for stock_num in stoList:
        if count < num_limit:
            url = boot_url + stock_num + '.html'
            html = get_html_text(url)
            soup = BeautifulSoup(html, 'html.parser')
            try:
                sto_info = soup.find_all('div', attrs={'class': 'stock-bets'})[0]
                name = sto_info.find_all('a', attrs={'class': 'bets-name'})[0]
                infoDict['股票名称'] = name.text.split()[0]
                keys = sto_info.find_all('dt')
                values = sto_info.find_all('dd')
                for i in range(len(keys)):
                    infoDict[keys[i].text] = values[i].text.split()[0]
                with open(file_path, 'a') as f:
                    f.write(str(infoDict) + '\n')
                    count = count + 1
                    print("\r当前进度: {:.2f}%".format(count * 100 / num_limit), end="")
            except:
                count = count + 1
                # traceback.print_exc()
                print("\r当前进度: {:.2f}%".format(count * 100 / num_limit), end="")
                continue
    return ""


def main():
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    file_path = 'stock_info.txt'
    stoList = []
    get_stock_list(stoList, stock_list_url)
    get_stock_info(stoList, stock_info_url, file_path,num_limit=50)
main()