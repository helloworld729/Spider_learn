import requests
from bs4 import BeautifulSoup

r = requests.get('http://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')
# for son in soup.body.descendants:
#     print(son)

i = 0
