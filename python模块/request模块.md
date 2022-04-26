# REQUEST基础

## 代理的使用

```python
import requests
from fake_useragent import UserAgent

url = 'https://www.baidu.com/s?ie=UTF-8&wd=ip'
headers = {
    'UserAgent': UserAgent().chrome
}
data_text = requests.get(url=url, headers=headers,proxies={'http':'202.55.5.209'}).text
print(data_text)
with open('1.html','w',encoding='gb2312') as f:
    f.write(data_text)
```



# 爬取樱花动漫番剧信息追加写入csv

```python
import requests
from fake_useragent import UserAgent
from lxml import etree
import pandas as pd


def fanjuxiangqing(url):
    headers = {
        'User-Agent': UserAgent().chrome
    }
    resp = requests.get(url=url, headers=headers).text
    tree = etree.HTML(resp)
    name = tree.xpath('/html/body/div[2]/div[2]/div[2]/h1/text()')
    name = ''.join(name)

    date = tree.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/span[1]//text()')
    date = ''.join(date)
    date = date.replace('\n', '')
    date = date.replace(' ', '')
    date = date.split(':')[1]

    gengxin = tree.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/p[2]/font/text()')
    gengxin = ''.join(gengxin)
    gengxin = gengxin[1:-1]

    gengxinz = tree.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/p[2]/text()')
    gengxinz = ''.join(gengxinz)
    gengxinz = gengxinz.split('：')[-1]

    leixing = tree.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/span[3]/a/text()')
    leixing = ','.join(leixing)
    fanju_xinxi = {
        '番名': name,
        '上映时间': date,
        '更新时间': gengxin,
        '更新至': gengxinz,
        '类型': leixing
    }
    return fanju_xinxi


def zhuye(url):
    headers = {
        'User-Agent': UserAgent().chrome
    }
    resp = requests.get(url=url, headers=headers).text
    tree = etree.HTML(resp)
    url_list = tree.xpath('/html/body/div[4]/div[2]/div[1]/ul/li/a[1]/@href')
    for i in range(0, len(url_list)):
        url_list[i] = 'https://www.yhdmp.me/' + url_list[i]
    return url_list


a = zhuye('https://www.yhdmp.me/list/?region=%E6%97%A5%E6%9C%AC')
print(a)
df = pd.DataFrame([['番名', '上映时间', '更新时间', '更新至', '类型']])
df.to_csv('樱花动漫.csv', header=False, index=False)
i = 0
for c in a:
    try:
        fj_data = fanjuxiangqing(c)
        df = pd.DataFrame([fj_data])
        # pandas追加方式写入
        df.to_csv('樱花动漫.csv', mode='a', header=False, index=False)
        print(i)
        i += 1
    except:
        print('终止')
print('获取完成')
```

# Ajax请求爬取豆瓣电影

```python
import requests
import pandas as pd

List = []
for i in range(20):
    url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'.format(
        str(i * 20))
    headers = {
        'Cookie': 'll="118255"; bid=XVECDtMh0-k; ct=y; _ga=GA1.2.57509567.1645879799; gr_user_id=f8e0af70-31aa-427e-b0fa-5872c41463da; douban-fav-remind=1; _vwo_uuid_v2=D51DAE856BF03A9658953080D2BB3C90B|1733155e54f18fb1882e7fa2ffc6ab44; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1648270064%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DmnAb56hHOZXwrsbSD6lbgvdKRgoiqBpfjrJWymw59SgJt_Yr6wvO8zsx3y_EhAtO%26wd%3D%26eqid%3Dbda029d2000a962d00000005623e9aec%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.57509567.1645879799.1647232953.1648270065.12; __utmb=30149280.0.10.1648270065; __utmc=30149280; __utmz=30149280.1648270065.12.10.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1683732533.1645879810.1647232953.1648270065.9; __utmb=223695111.0.10.1648270065; __utmc=223695111; __utmz=223695111.1648270065.9.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=f7601e1cc87fd2c1.1645879810.8.1648270079.1647232953.',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    }
    resp = requests.get(url=url, headers=headers).json()
    # print(resp)
    for a in resp:
        name = a['title']
        leixing = a['types']
        LX = ''
        for tp in leixing:
            LX = LX + '/' + tp
        pingfen = a["score"]
        yanyuan = a["actors"]
        YY = ''
        for yy in yanyuan:
            YY = YY + '/' + yy
        nianfen = a["release_date"]
        dara_dict = {
            '电影名': name,
            '类型': LX,
            '年份': nianfen,
            '演员': YY,
            '评分': pingfen
        }
        List.append(dara_dict)
    print('第{}页完成'.format(str(i + 1)))
df = pd.DataFrame(List)
df.to_csv('汇总.csv')
```

