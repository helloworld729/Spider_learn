import requests

def trans_ipaddress():
    """

    :return:
    """
    url = 'http://ip.tool.chinaz.com/?ip='
    try:
        r = requests.get(url + '223.3.77.161')
        r.encoding = r.apparent_encoding
        print("网络状态码： {}".format(r.status_code))
        print(r.text[17275:17330])
        r.close()
    except:
        print('get_failure')

trans_ipaddress()