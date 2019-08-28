import requests
import re

## 程序结构设计
#### 步骤1：提交商品搜索请求，循环获取页面
#### 步骤2：对于每个页面，提取商品名称和价格信息
#### 步骤3：将信息输出到屏幕

# 获取网页
def get_html_text(url, kv):
    try:
        r = requests.get(url, headers=kv, timeout=30)  # headers
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 网页解析
def parsePage(info_list, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)  # 匹配每个位置是 数字或者点 的 任意长度 字符串
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)  # 匹配若干字符 ?：表示最小匹配
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            info_list.append([price, title])
    except:
        pass


# 信息输出
def print_info(infolist):
    pf = "{:4}\t{:8}\t{:16}"
    print(pf.format("序号", "价格", "商品名称"))
    count = 0
    for g in infolist:
        count = count + 1
        print(pf.format(count, g[0], g[1]))


def main():
    info_list = []
    depth = 1
    good = '男鞋'
    kv = {'cookie': 'thw=cn; cna=PdvfFbP8qmcCAd8DTaG+cEn8; v=0; t=eb60b025571ebb9dc3322b10c80858ac; cookie2=1891b6fa7ced0e6ebcaa05f5b11b77d0; _tb_token_=57b16e34eeeb; unb=2002399149; uc3=nk2=q5ccXpBE&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dBy3MNgeVDnvIThW0%3D&id2=UUjRIG%2B7mmYCGw%3D%3D; csg=2ed2c55f; lgc=%5Cu4EFB%5Cu70B3%5Cu5148; cookie17=UUjRIG%2B7mmYCGw%3D%3D; dnk=%5Cu4EFB%5Cu70B3%5Cu5148; skt=1ccc3f4644d349c2; existShop=MTU2NjcwNTA3OA%3D%3D; uc4=id4=0%40U2ozl6EX%2BOswIFh%2FQnvHsJgSJ3sS&nk4=0%40qSIoWVsEltd4PVLrO3RXLYs%3D; tracknick=%5Cu4EFB%5Cu70B3%5Cu5148; _cc_=WqG3DMC9EA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=%E5%85%8899; _nk_=%5Cu4EFB%5Cu70B3%5Cu5148; cookie1=UINO14AbOLBtlI6nnlE3EPmakbbnbtKHqHJareoNkiY%3D; enc=n%2FOKevWY8CEAmAyO%2BiOXy6de2a3MM0rfRXVsOExbrXB%2BdEI7TxggfGdMRT2jifUdKaRaNvKZG0iudAol5dXtKQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=74_1; swfstore=217968; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=99B39E924A302464DB0EE38F49597828; uc1=cookie14=UoTaHoyydCFjyQ%3D%3D&lng=zh_CN&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&existShop=false&cookie21=W5iHLLyFeYZ1WM9hVLhR&tag=8&cookie15=V32FPkk%2Fw0dUvg%3D%3D&pas=0; isg=BHFxKh1OiGL22yR2xrpdwRdegP3UXahxOIDYS1OGATjsepPMm658ocXYmE65sn0I; l=cBO1f8RVqJ2tfN0SBOCwdkf1SJ_TlIRVguP3Y6AWi_5QT1Av2i_OkorMeev6cjWFTsYB4CWT0IpTze3L8yDXnSFpne1VivC..; whl=-1%260%260%261566706689827',
          'user-agent': "Mozilla/5.0"}
    start_url = 'https://s.taobao.com/search?q=' + good

    for epoch in range(depth):
        try:
            url = start_url + '&s=' + str(44*epoch)
            html = get_html_text(url, kv)
            parsePage(info_list, html)
        except:
            continue
    print_info(info_list)


main()