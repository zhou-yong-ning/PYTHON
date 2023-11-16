import requests


url = 'http://59.208.147.83:7090/risk-census/building/getCountryHouse?bh=e8410386c49edb4756f126fe21341d29&xzqdm=420281'
headers = {
    'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'Appversion': 'pc',
    'Authorization': 'Bearer 2701a323-b32e-42c0-a09c-24ff43a1e25f',
    'Connection': 'keep-alive',
    'Dnt': '1',
    'Host': '59.208.147.83:7090',
    'Origin': 'http://59.208.147.83:18089'
}
data_text = requests.get(url=url, headers=headers).text
print(data_text)
with open('1.txt', 'w', encoding='utf-8') as f:
    f.write(data_text)
