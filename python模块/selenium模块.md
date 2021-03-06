# selenium模块

## 初步使用

```python
# 传统方法会报错
# 出现 DeprecationWarning 警告的类型错误：该类型的警告大多属于版本已经更新，所使用的方法过时。
# 查询当前版本重构后的函数，是之前的 executable_path 被重构到了 Service 函数里
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from lxml import etree
from time import sleep

# 尝试传参
s = Service("chromedriver.exe")
# 实例化一个浏览器驱动程序
bro = webdriver.Chrome(service=s)
# 让浏览器发起一个指定url请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')
# 如果定位的标签位于iframe中则需要通过以下操作定位
# bro.switch_to.iframe('')#切换标签定位的作用域，''内复制网页元素id，后面定位标签
# 获取浏览器当前页面源码数据
page_text = bro.page_source
# xpath解析获取指定数据
tree = etree.HTML(page_text)
name_list = tree.xpath('//*[@id="gzlist"]/li/dl/@title')
sleep(2)
bro.quit()
for i in name_list:
    print(i)
```

## selenium自动登录百度(查看某元素是否出现)

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.baidu.com/")
tag_denglu = driver.find_element(By.ID, "s-top-loginbtn")
tag_denglu.click()

# 方法一
while True:
    if EC.presence_of_element_located((By.ID, "TANGRAM__PSP_11__userName")):
        sleep(1)
        driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys('176****7572')
        driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys('***********')
        break
# 方法二
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "TANGRAM__PSP_11__userName")))
driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys('176****7572')
driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys('***********')

denglu_btn = driver.find_element(By.ID, "TANGRAM__PSP_11__submit")
denglu_btn.click()
sleep(5.1)
driver.quit()
# 回退与前进
browser.back()
browser.forward()
# 刷新
driver.refresh()

# from selenium.webdriver.support import expected_conditions as EC
# driver.find_element_by_id('kw').is_displayed()  # 查看元素是否可见
# EC.presence_of_element_located((By.ID, "kw"))  # 查看某个元素是否存在
# EC.element_to_be_clickable()  # 查看元素是否可点击
# EC.element_located_to_be_selected((By.ID, "kw"))  # 某个预期元素是否被选中
# 补充：
# # frame可见并切换到该frame上
# EC.frame_to_be_available_and_switch_to_it
# # 元素可以点击，常用于按键
# EC.element_to_be_clickable
# # 元素出现，只要一个符合条件的元素加载出来就通过
# EC.presence_of_element_located
# # 元素出现，须所有符合条件的元素都加载出来，这个基本上就是你爬取的最主要内容了
# EC.presence_of_all_elements_located
# # 判断某段文本是否出现在某元素中，常用于判断输入页数与实际高亮页数是否一致
# EC.text_to_be_present_in_element
```

## selenium-Windows窗口跳转方法

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service('chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.52pojie.cn/')
tag_sousuo = browser.find_element(By.ID, 'scbar_txt')
tag_sousuo.send_keys('python')
tag_sousuotb = browser.find_element(By.ID, 'scbar_btn')
tag_sousuotb.click()
# selenium自动化访问跳转新窗口、新标签的方法——切换句柄
# 通过Windows窗口的index区分，从0开始计
windows = browser.window_handles  # 获取所有窗口句柄列表
browser.switch_to.window(windows[1]) # browser切换至列表对应的页面
tag_sousuotb1 = browser.find_element(By.XPATH, '//*[@id="results"]/div[1]/h3/a') # 通过xpath定位元素
tag_sousuotb1.click()
```

## selenium选择下拉列表

```python

# 1. 使用Webdriver提供的Select类的方法：# 两种方法任选其一，都是指向同一个文件
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select 

# 2 Select类提供了3个方法用于选择下拉选择框中的其一
select_by_value(value)
select_by_index(index)
select_by_visible_text(text)

# 3 比如选择篮球运动员选项：
# 实例化一个Select类的对象
selector = Select(driver.find_element_by_id("selectdemo"))

# 下面三种方法用于选择
selector.select_by_index("2")  # 通过index进行选择,index从0开始
selector.select_by_value("210103")  # 通过value属性值进行选择
selector.select_by_visible_text("篮球运动员")  # 通过标签显示的text进行选择 

# 主要使用select_by_index()的时候，如果option中有index属性，会优先通过index属性选择
selector.select_by_visible_text("")  # 该方法可用于取消选择 
# Select类还提供了一些用于取消选中的方法
# 注意：
# 反选（deselect）取消操作只适用于添加了multiple的下拉框，否则会报错
# raise NotImplementedError("You may only deselect options of a multi-select")
# NotImplementedError: You may only deselect options of a multi-select
deselect_all()  # 取消全选
deselect_by_value(value) # 通过value属性取消选择
deselect_by_index(index) # 通过index取消选择
deselect_by_visible_text(text) # 通过text取消选择 
```

```python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from selenium.webdriver.support.ui import Select
# 或者直接从select导入
from selenium.webdriver.support.select import Select

s = Service("chromedriver.exe")
Browser = webdriver.Chrome(service=s)
Browser.get("http://sahitest.com/demo/selectTest.htm")
# 等待网页指定元素出现（显式等待）
WebDriverWait(Browser, 10).until(EC.presence_of_element_located((By.ID,"s1Id")))
print('加载完成')
Browser.get('http://sahitest.com/demo/selectTest.htm')
# 实例化Select
s1 = Select(Browser.find_element(By.ID,'s1Id'))
# # 选择第二个选项o1
# s1.select_by_index(2)
s2 = Select(Browser.find_element(By.ID,'s2Id'))
# # 选择第二个选项o1
# s2.select_by_index(1)
s3 = Select(Browser.find_element(By.ID,'s3Id'))
# # 选择第二个选项o1
# s3.select_by_index(3)

# 查看选择框的默认值/打印当前下拉框选择值
print (s1.first_selected_option.text)
print (s2.first_selected_option.text)
print (s3.first_selected_option.text)
# 实例化Select
s1 = Select(Browser.find_element(By.ID,'s1Id'))
# 选择第二个选项o1
s1.select_by_visible_text('o1')
s2 = Select(Browser.find_element(By.ID,'s2Id'))
# 选择第二个选项o1
s2.select_by_visible_text('o3')
s3 = Select(Browser.find_element(By.ID,'s3Id'))
# 选择第二个选项o1
s3.select_by_visible_text('o3')
print (s1.first_selected_option.text)
print (s2.first_selected_option.text)
print (s3.first_selected_option.text)
# 注意：
# 反选（deselect）取消操作只适用于添加了multiple的下拉框，否则会报错
# raise NotImplementedError("You may only deselect options of a multi-select")
# NotImplementedError: You may only deselect options of a multi-select
# 实例化Select
sleep(2)
s1 = Select(Browser.find_element(By.ID,'s1Id'))
# 通过文本选择方式清除选项
s1.select_by_visible_text('')
s2 = Select(Browser.find_element(By.ID,'s2Id'))
# 清除选项
s2.select_by_visible_text('')
s3 = Select(Browser.find_element(By.ID,'s3Id'))
# 清除选项
s3.select_by_visible_text('')
# 打印当前下拉框选择值
print (s1.first_selected_option.text)
print (s2.first_selected_option.text)
print (s3.first_selected_option.text)
sleep(3)
```
## Selenium判断单选框是否选中

```python
# 首先判断该元素有没有选中，可以用is_selected方法来获取该元素有没有被选中
input=driver.find_element_by_css_selector( 'input[value=car]')
selected=input.is_selected()  #判断是否选中

if selected:
    print('已经选中了,无需点击')
else:
    print('没有选中，需要点击')
    input.click()

```
## Selenium 获取一组元素然后循环点击

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from lxml import etree
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service("chromedriver.exe")
Browser = webdriver.Chrome(service=s)
Browser.get("https://pic.netbian.com/")
# 显式等待
WebDriverWait(Browser, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/a")))
item = Browser.find_elements(By.XPATH,'//*[@id="main"]/div[3]/ul/li')
# 循环个数，range函数从0递增
for i in range(len(item)-1):
    # 每次循环，都重新获取元素，防止元素失效或者页面刷新后元素改变了
    item = Browser.find_elements(By.XPATH,'//*[@id="main"]/div[3]/ul/li')
    # 循环点击获取的元素
    item[i].click()
    sleep(0.5)
    # # 打印每次获取元素，调试用
    # print(f'{i}:\t{item[i]}')  
    windows = Browser.window_handles  # 获取所有窗口句柄列表
    Browser.switch_to.window(windows[1]) # browser切换至列表对应的页面
    page_text = Browser.page_source
    tree = etree.HTML(page_text)
    name = tree.xpath('//*[@id="main"]/div[2]/div[1]/div[1]/h1/text()')
    print(name)
    Browser.close() # 关闭当前页面
    windows = Browser.window_handles  # 获取所有窗口句柄列表
    Browser.switch_to.window(windows[0]) # browser切换至列表对应的页面
```
