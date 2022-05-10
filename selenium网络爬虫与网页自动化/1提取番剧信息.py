from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from lxml import etree
import requests
from fake_useragent import UserAgent
# from selenium.webdriver.common.keys import Keys
# from multiprocessing import Pool

def datakh(tree,fzxpath):
    data_zhenghe = tree.xpath(fzxpath)
    data_zhenghe = ''.join(data_zhenghe)
    data_zhenghe = data_zhenghe.replace(' ','')
    data_zhenghe = data_zhenghe.replace('\n','')
    return data_zhenghe

class fanju_data():
    def fjxx(self,page):
        tree = etree.HTML(page)
        fanju_name = tree.xpath('/html/body/div[2]/div[2]/div[2]/h1/text()')
        fanju_leixing = datakh(tree,'/html/body/div[2]/div[2]/div[2]/div[2]/span[3]//text()')
        fanju_date = datakh(tree,'/html/body/div[2]/div[2]/div[2]/div[2]/span[1]//text()')
        fanju_lable = datakh(tree,'/html/body/div[2]/div[2]/div[2]/div[2]/span[5]//text()')
        fanju_genxin = datakh(tree,'/html/body/div[2]/div[2]/div[2]/div[2]/p[2]//text()')
        fanju_jianjie = tree.xpath('/html/body/div[2]/div[2]/div[9]/text()')
        dada = {
            '番剧名':fanju_name,
            '番剧类型':fanju_leixing,
            '番剧日期':fanju_date,
            '番剧标签':fanju_lable,
            '番剧更新':fanju_genxin,
            '番剧简介':fanju_jianjie
        }
        return dada
    def tupian(self,page):
        tree = etree.HTML(page)
        Url = tree.xpath('/html/body/div[2]/div[2]/div[1]/img/@src')
        src_url = 'https:' + Url[0]
        src_headers = {
            'User-Agent': UserAgent().chrome
        }
        src_resp = requests.get(url=src_url, headers=src_headers).content
        name = src_url.split('/')[-1]
        with open('./新建文件夹/'+name, 'wb') as f:
            f.write(src_resp)
        print('下载成功')


s = Service("C:\\Users\\zhou\\Desktop\\selenium\\chromedriver.exe")  # 尝试传参
bro = webdriver.Chrome(service=s)  # 实例化一个浏览器驱动程序
bro.get('https://www.yhdmp.me/list/?region=%E6%97%A5%E6%9C%AC')  # 让浏览器发起一个指定url请求
WebDriverWait(bro, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div[1]/ul/li/h2/a")))  # 显式等待页面加载
sleep(1)
item = bro.find_elements(By.XPATH, '/html/body/div[4]/div[2]/div[1]/ul/li/h2/a')  # 获取需要点击的要素列表
for i in range(len(item)):
    # 每次循环，都重新获取元素，防止元素失效或者页面刷新后元素改变了
    item = bro.find_elements(By.XPATH, '/html/body/div[4]/div[2]/div[1]/ul/li/h2/a')
    item[i].click()  # 循环点击获取的元素
    WebDriverWait(bro, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[8]/h2")))     # 显式等待网页某一元素加载完成
    sleep(0.5)
    page_text = bro.page_source
    a = fanju_data() # 实例化一个对象
    fanju = a.fjxx(page_text) # 调用fanju_data类中的fjxx方法
    print(fanju)
    a.tupian(page_text)
    bro.back()  # 返回上个页面
    sleep(1)
    # 下面方法实现页面滚动
    # 方法一
    # bro.execute_script('window.scrollTo(0,133)')    # 执行一组js程序,页面向左移动0像素，向下移动133像素
    # 方法二
    # page_body = bro.find_element_by_xpath('/html/body')
    # page_body.send_keys(Keys.SPACE)  # 点击空白处并且按下空格键实现翻页效果
    sleep(0.5)
