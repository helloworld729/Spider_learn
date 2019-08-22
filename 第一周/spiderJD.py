import requests

url = "https://item.jd.com/48230531185.html"
try:
    # r = requests.get(url)
    r = requests.request(method="get", url=url)  # 两者等价
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:500])
    # print(header['Content-Type'])
except:
    print("spider fail")

