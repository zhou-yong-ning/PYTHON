# 1、工作簿

## （1）创建工作簿

```python
# workbook为对象
workbook=openpyxl.Workbook('name.xlsx')
workbook.save(path)
```

## （2）打开工作簿

```python
# workbook、woorksheet为对象
workbook =openpyxl.load_workbook('filename.xlsx')
woorksheet = workbook ['Sheet1']
```

| **属性**       | **作用**                                         |
| -------------- | ------------------------------------------------ |
| **active**     | **获取当前活跃的Worksheet**                      |
| **worksheets** | **以列表的形式返回所有的Worksheet(表格)**        |
| **data_only**  | **默认为False,为True时只读取数据不显示公式**     |
| **read_only**  | **判断是否以read_only模式打开Excel文档**         |
| **encoding**   | **获取文档的字符集编码**                         |
| **properties** | **获取文档的元数据，如标题，创建者，创建日期等** |
| **sheetnames** | **获取工作簿中的表（列表）**                     |

| 方法                   | 作用                              |
| ---------------------- | --------------------------------- |
| **workbook.sheetname** | **获取所有表格的名称**            |
| **workbook['Sheet1']** | **通过表格名称获取Worksheet对象** |
| **workbook.active**    | **获取活跃的表格**                |
| **remove**             | **删除一个工作表对象【对象】**    |
| **create_sheet**       | **创建一个空的表格【表名】**      |
| **copy_worksheet**     | **在Workbook内拷贝表格【对象】**  |

# 2、工作表

```python
#获取工作表名称
workbook.sheetname
#指定工作表
workbook['Sheet1']
#获取当前活跃的工作表
workbook.active
#获取工作表名称
sheetname.title
```

| 属性             | 作用                                                         |
| ---------------- | ------------------------------------------------------------ |
| **title**        | **工作表的名称**                                             |
| **dimensions**   | **表格的大小，这里的大小是指含有数据的表格的大小，即：左上角的坐标:右下角的坐标** |
| **max_row**      | **表格的最大行**                                             |
| **min_row**      | **表格的最小行**                                             |
| **max_column**   | **表格的最大列**                                             |
| **min_column**   | **表格的最小列**                                             |
| **rows**         | **按行获取单元格(Cell对象) - 生成器**     **worksheet.rows** |
| **columns**      | **按列获取单元格(Cell对象) - 生成器**     **worksheet.columns** |
| **freeze_panes** | **冻结窗格**    **worksheet.freeze_panes = "C3"**            |
| **values**       | **按行获取表格的内容(数据) - 生成器**                        |

**freeze_panes参数比较特别，主要用于在表格较大时冻结顶部的行或左边的行。对于冻结的行，在用户滚动时，是始终可见**

**的，可以设置为一个Cell对象或一个端元个坐标的字符串，单元格上面的行和左边的列将会冻结(单元格所在的行和列不会被冻**

**结)。例如我们要冻结第一行那么设置A2为freeze_panes，如果要冻结第一列，freeze_panes取值为B1，如果要同时冻结第一**

**行和第一列，那么需要设置B2为freeze_panes，freeze_panes值为none时 表示 不冻结任何列。**

| **方法**           | 作用                                                         |
| ------------------ | ------------------------------------------------------------ |
| **iter_rows**      | **按行获取所有单元格，内置属性有(min_row,max_row,min_col,max_col)** |
| **iter_columns**   | **按列获取所有的单元格**                                     |
| **append**         | **在表格末尾添加数据**                                       |
| **merged_cells**   | **合并多个单元格**                                           |
| **unmerged_cells** | **移除合并的单元格**                                         |

# 3、单元格

| 属性           | 作用               |
| -------------- | ------------------ |
| **row**        | **单元格所在的行** |
| **column**     | **单元格所在的列** |
| **value**      | **单元格的值**     |
| **coordinate** | **单元格的坐标**   |

# 01、**工作簿新建、保存和打开**

## （1）新建和保存

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.Workbook(file_path)
workbook.save(r"C:\Users\zhou\Desktop\笔记\新建文件夹\示例.xlsx")
```

## （2）打开工作簿

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet']
print(worksheet)
```

## （3）获取当前活跃的工作表

```python
import openpyxl as vb
file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook.active
print(worksheet)
```

# 02、**工作表的创建、删除、复制**

## **一、显示工作簿中所有的工作表和表名**

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet_list = workbook.worksheets
print(worksheet_list)
for i in worksheet_list:
    print(i.title)
```

## **二、删除指定工作表**

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet_list = workbook.worksheets
# 以下两种方法都可以
# workbook.remove(worksheet_list[0])
workbook.remove(workbook['Sheet'])
workbook.save(file_path)
```

## **三、新建指定工作表**

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
workbook.create_sheet('创建工作表')
workbook.save(file_path)
```

## **四、复制指定工作表**

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
copy_sheet = workbook.copy_worksheet(workbook['Sheet1'])
copy_sheet.title = '复制表'
workbook.save(file_path)
```

# 03、工作表中单元格操作

## **一、获取一个单元格的值**

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
# 以下三种方式都可以
# cell_value = worksheet['A1'].value
cell_value = worksheet.cell(row = 1,column = 1).value
# cell_value = worksheet.cell(1,1).value
print(cell_value)
```

## **二、获取第二列1.3.5.7行的值**

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
for i in range(1, 8, 2):
    cell_value = worksheet.cell(row=i, column=2).value
    print(cell_value)
```

