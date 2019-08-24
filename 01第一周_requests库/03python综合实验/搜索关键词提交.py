import requests
# 百度：url = 'http://www.baidu.com/s？wd=keyworld'
def search_baidu():
    url = 'http://www.baidu.com/s'

    try:
        kv = {'wd': 'China'}
        r = requests.get(url, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print("请求的网站是： {}".format(r.request.url))
        print(r.text)
    except:
        print('search_failure')

search_baidu()