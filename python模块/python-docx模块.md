# python-docx 制作word文档

## 读取word文本

```python
#!/usr/bin/env python
# coding: utf-8

import docx

# 获取文档对象
file = docx.Document("test1.docx")
print("段落数:" + str(len(file.paragraphs)))  # 段落数为*，每个回车隔离一段

# 输出每一段的内容
for para in file.paragraphs:
    print(para.text)

# 输出段落编号及段落内容
for i in range(len(file.paragraphs)):
    print("第" + str(i+1) + "段的内容是：" + file.paragraphs[i].text)
```

### 实战提取简历信息

```python
from docx import Document
import os
import pandas as pd
from win32com import client as wc
from time import sleep

# 获取当前.py文件所在绝对路径
Current_Folder_path = os.getcwd()
# 在当前文件夹内新建名为”New Folder“的文件夹
if not os.path.exists(Current_Folder_path + '\\New Folder'):
    os.mkdir(Current_Folder_path + '\\New Folder')
# 获取指定文件夹内所有文件
file_list = os.listdir(Current_Folder_path)
# (以下注释部分可以将doc转为docx)
# # 利用推导式获取所有后缀为”.doc“的文件
# doc_list = [a for a in file_list if a.endswith('.doc')]
# word = wc.Dispatch("Word.Application")  # 打开word应用程序
# for A in doc_list:
#     word = wc.Dispatch("Word.Application")  # 打开word应用程序
#     doc = word.Documents.Open(Current_Folder_path + "\\" + A)  # 打开word文件,必需绝对路径
#     A = A.replace('.doc', '.docx')
#     doc.SaveAs(Current_Folder_path + "\\" + A, 12)  # 另存为后缀为".docx"的文件，其中参数12指docx文件,必需绝对路径
#     doc.Close()  # 关闭原来word文件
#     print(A + "转换完成")
# word.Quit()  # 关闭原来word应用程序
# 利用推导式获取所有后缀为”.docx“的文件
docx_list = [a for a in file_list if a.endswith('.docx')]
word_list = []  # 建立空列表，存放每个word的数据字典
for i in docx_list:
    file = Document(i)  # 调用Document函数，读取文件
    table = file.tables[-1]  # 获取文件中的表格集，获取表格集中的第一个表格
    word_dict = {
        "A": table.cell(1, 5).text,
        "B": table.cell(9, 3).text,
        "C": table.cell(12, 2).text,
        "D": table.cell(15, 4).text
    }
    word_list.append(word_dict)  # 往列表添加数据字典
    print(i + "提取完成")
df = pd.DataFrame(word_list)
df.to_csv(Current_Folder_path + "\\New Folder\\" + "数据汇总.csv")

```

## 制作word文本

### 1.创建文档

```python
from docx import Document
document = Document()
document.save('ceshi.docx')  #保存文档
```

### 2.添加标题

```python
from docx import Document

document = Document()
document.add_heading('爬虫与数据分析', 0)  # 添加标题，数字代表第几级标题
document.save('ceshi.docx')  # 保存文档
```

但是，这个有个问题是标题下面有一条横线，对于重度强迫症的我是无法容忍的。所以我们可以直接添加段落文字表示标题

### 3.添加段落文字

```python
from docx import Document

document = Document()
document.add_paragraph('爬虫与数据分析')  # 添加段落
document.save('ceshi.docx')  # 保存文档
```

### 4.设置字体大小

```python
from docx import Document
from docx.shared import Pt

document = Document()
p = document.add_paragraph()
run = p.add_run('爬虫与数据分析')  # 使用add_run添加文字
run.font.size = Pt(26)  # 设置字体大小26像素
document.save('ceshi.docx')
```

#### word中字体大小（pt）和网页中css设置font-size时用的px大小对应关系

pt与px转换关系为 1px= 0.75pt。

所以word中五号字体（10.5pt）在网页中对应的大小为font-size:14px。（10.5 / 0.75 = 14)

		初号44pt	小初36pt	一号26pt	小一24pt	二号22pt	小二18pt	三号16pt	小三15pt
	
		四号14pt	小四12pt	五号10.5pt	小五9pt	六号7.5pt	小六6.5pt	七号5.5pt	八号5pt

### 5.设置对齐方式

```python
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

document = Document()
p = document.add_paragraph() 
run = p.add_run('爬虫与数据分析')  # 使用add_run方法添加段落
run.font.size = Pt(26)  # 设置字体
# 设置对齐方式（.CENTER 居中对齐/.LEFT 左对齐/.RIGHT 右对齐）
p.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER #段落文字居中设置
document.save('ceshi.docx')
```

### 6.设置字体加粗

```python
run.bold = True  # 字体加粗
run.italic = True #字体倾斜
```

### 7.设置字体

```python
from docx.oxml.ns import qn

#设置整个文档字体
document.styles['Normal'].font.name = '宋体'  # 设置字体
document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
```

### 8.设置文字颜色

```python
from docx.shared import RGBColor

run.font.color.rgb = RGBColor(255,0,0) #颜色设置，这里是用RGB颜色
```

### 9.综合练习一

```python
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from docx.shared import RGBColor
from docx.shared import Inches

document = Document()
p = document.add_paragraph()
run = p.add_run('python爬虫与数据分析')  # 使用add_run添加文字
run.font.size = Pt(26)  # 字体大小设置，和word里面的字号相对应，小一
p.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # 段落文字居中设置
run.bold = True  # 字体加粗
document.styles['Normal'].font.name = '宋体'  # 设置字体
document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
run.font.color.rgb = RGBColor(255, 0, 0)  # 颜色设置，这里是用RGB颜色

pic = document.add_picture('哆啦A梦.jpg', width=Inches(5))  # 添加图片，设置宽度（长度等比例放大缩小）
last_paragraph = document.paragraphs[-1]
last_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # 图片居中设置

p = document.add_paragraph()
run = p.add_run('python简介')
run.font.size = Pt(22)  # 二号
run.bold = True

p = document.add_paragraph()
run = p.add_run(
    'Python由荷兰数学和计算机科学研究学会的吉多·范罗苏姆 于1990 年代初设计，作为一门叫做ABC语言的替代品。 Python提供了高效的高级数据结构，还能简单有效地面向对象编程。Python语法和动态类型，以及解释型语言的本质，使它成为多数平台上写脚本和快速开发应用的编程语言， 随着版本的不断更新和语言新功能的添加，逐渐被用于独立的、大型项目的开发。')
p_format = p.paragraph_format
p_format.first_line_indent = Inches(0.2)  # 首行缩进

document.save('ceshi.docx')  # 保存文档

```

### 10.添加表格

关于表格样式，可以参考链接：https://blog.csdn.net/ibiao/article/details/78595295

```python
from docx import Document
from docx.shared import Pt
from docx.shared import RGBColor

document = Document()
table = document.add_table(rows=4, cols=5)  #4行5列的表格
table.style = document.styles['Table Grid']  #设置表格样式
# 封装表格字体加粗函数{同理可设置字体大小，对齐方式}
def th(x,y,content):
    """
    th样式
    :param x: x坐标
    :param y: y坐标
    :param content: 内容
    :return: None
    """
    # print(grid,content)
    run = table.cell(x,y).paragraphs[0].add_run(content)
    run.bold = True  # 加粗
def td_red(table,x, y,content):
    """
    td红色字体
    :param table: 表格对象
    :param x: x坐标
    :param y: y坐标
    :param content: 内容
    :return: None
    """
    run = table.cell(x, y).paragraphs[0].add_run(content)
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(255, 0, 0)
th(0,0,"歌曲")
th(0,1,"演唱者")
th(0,2,"作曲")
th(0,3,"作词")
th(0,4,"类型")

table.cell(1,0).text = "《风起时》"
# table.cell(1,1).text = "胡歌"
td_red(table,1,1,"胡歌")
table.cell(1,2).text = "孟可"
table.cell(1,3).text = "海宴"
table.cell(1,4).text = "主题曲、片尾曲"

table.cell(2,0).text = "《红颜旧》"
table.cell(2,1).text = "刘涛"
table.cell(2,2).text = "赵佳霖"
table.cell(2,3).text = "袁亮"
table.cell(2,4).text = "插曲"

table.cell(3,0).text = "《赤血长殷》"
table.cell(3,1).text = "王凯"
table.cell(3,2).text = "于海航"
table.cell(3,3).text = "清彦、冰封"
table.cell(3,4).text = "插曲"

document.save('ceshi.docx')  #保存文档
```

### 11.综合练习二

```python
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from docx.shared import RGBColor
from docx.shared import Inches

document = Document()
p = document.add_paragraph()
run = p.add_run('python爬虫与数据分析')  # 使用add_run添加文字
run.font.size = Pt(26)  # 字体大小设置，和word里面的字号相对应，小一
p.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # 段落文字居中设置
run.bold = True  # 字体加粗
document.styles['Normal'].font.name = '宋体'  # 设置字体
document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
run.font.color.rgb = RGBColor(255, 0, 0)  # 颜色设置，这里是用RGB颜色

pic = document.add_picture('哆啦A梦.jpg', width=Inches(5))  # 添加图片，设置宽度（长度等比例放大缩小）
last_paragraph = document.paragraphs[-1]
last_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # 图片居中设置

p = document.add_paragraph()
run = p.add_run('python简介')
run.font.size = Pt(22)  # 二号
run.bold = True

p = document.add_paragraph()
run = p.add_run(
    'Python由荷兰数学和计算机科学研究学会的吉多·范罗苏姆 于1990 年代初设计，作为一门叫做ABC语言的替代品。 Python提供了高效的高级数据结构，还能简单有效地面向对象编程。Python语法和动态类型，以及解释型语言的本质，使它成为多数平台上写脚本和快速开发应用的编程语言， 随着版本的不断更新和语言新功能的添加，逐渐被用于独立的、大型项目的开发。')
p_format = p.paragraph_format
p_format.first_line_indent = Inches(0.2)  # 首行缩进

document.save('ceshi.docx')  # 保存文档

#实际效果见数据文件ceshi.docx
```

