import httpx
import json
import requests


url="https://www.cnblogs.com/yoyoketang/"

resp=requests.get(url)
resp.encoding = 'utf-8'
print(resp.url)
print(json.dumps(resp.content))












