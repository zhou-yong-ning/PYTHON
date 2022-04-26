# 爬取彼岸图网壁纸

```python
import requests
from lxml import etree
from fake_useragent import UserAgent

for a in range(10,30):
    url = 'https://pic.netbian.com/4kdongman/index_{}.html'.format(a)
    headers = {
        'User-Agent': UserAgent().chrome
    }
    resp = requests.get(url=url, headers=headers).text
    # print(resp)
    tree = etree.HTML(resp)
    src_list = tree.xpath('//*[@id="main"]/div/ul/li/a/img/@src')
    for i in src_list:
        src_url = 'https://pic.netbian.com' + i
        src_headers = {
            'User-Agent': UserAgent().chrome
        }
        src_resp = requests.get(url=src_url, headers=src_headers).content
        name = src_url.split('/')[-1]
        with open('./新建文件夹/' + name, 'wb') as f:
            f.write(src_resp)
        print('下载成功')
```

# 爬取药监总局化妆品

```python
import requests
from fake_useragent import UserAgent
import pandas as pd
import time

url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
List = []
for a in range(20):
    UA = UserAgent().chrome
    dada = {
        'on': 'true',
        'page': str(a+1),
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
    }
    headers = {
        'User-Agengt': UA
    }
    resp = requests.post(url=url, data=dada, headers=headers).json()
    resp_list = resp['list']
    id_list = []
    time.sleep(1)
    for i in resp_list:
        id_list.append(i['ID'])
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    headers_post = {
        'User-Agengt': UserAgent().chrome
    }
    for ID in id_list:
        dada_post = {
            'id': ID
        }
        post_resp = requests.post(url=post_url, headers=headers_post, data=dada_post).json()
        # print(post_resp)
        dict_data = {
            '负责人': post_resp['legalPerson'],
            '企业名称': post_resp['epsName'],
            '许可证编号': post_resp['productSn'],
            '生产许可项目': post_resp['certStr'],
            '企业住所': post_resp['epsAddress'],
            '发证机关': post_resp['qfManagerName'],
        }
        List.append(dict_data)
        print('导出成功')

df = pd.DataFrame(List)
df.to_csv('药监总局数据.csv')
```

