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

## 三、获取一个区域的单元格

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
cell_range = worksheet['A1:H26']
# 按行选定区域
# cell_range = worksheet['1:26']
# 按列选定区域
# cell_range = worksheet['A:H']
for row_data in cell_range:
    for cell_data in row_data:
        print(cell_data.value)
```

```python
# 使用list(worksheet.values)
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
print(list(worksheet.values))
```

```python
# .iter_rows(min_row=最低行数，max_row=最高行数，min_col=最低列数，max_col=最高列数)
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
for row_data in worksheet.iter_rows(min_row=1, max_row=26, max_col=8, min_col=1):
    for cell_data in row_data:
        print(cell_data.value)
```

```python
# .iter_cols(min_row=最低行数，max_row=最高行数，min_col=最低列数，max_col=最高列数)
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
for col_data in worksheet.iter_cols(min_row=1, max_row=26, max_col=8, min_col=1):
    for cell_data in col_data:
        print(cell_data.value)

```

## 四、依次获取每一行每一列的值

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
for row_data in worksheet.rows:
    for cell_data in row_data:
        print(cell_data.value)
for col_data in worksheet.columns:
    for cell_data in col_data:
        print(cell_data.value)
```

## 五、字母与数字间的转换

```python
import openpyxl as vb
# 根据列的数字返回字母
numtoletter = vb.utils.get_column_letter(2)
print(numtoletter)
# 根据字母返回列的数字
lettertonum= vb.utils.column_index_from_string('D')
print(lettertonum)
```

## 六、读取数据

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
max_row = worksheet.max_row
max_col = worksheet.max_column
A1_value = worksheet['A1'].value
A1_value2 = worksheet.cell(1, 1).value
A1_col = worksheet['A1'].column
A1_row = worksheet['A1'].row
# 获取C列所有数据
list1 = []
for i in worksheet['C']:
    list1.append(i.value)
# 获取第1行所有数据
list2 = []
for i in worksheet[1]:
    list2.append(i.value)
# 获取所有数据
list3 = []
for row in worksheet.rows:
    for cell in row:
        list3.append(cell.value)
print(list3)
```

## 七、写入数据

```python
# 在指定单元格写入数据
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
worksheet.cell(1,1, value='zhou')
worksheet['A1'] = 'yong'
workbook.save(file_path)
```

```python
# 在最后一行写入数据
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
worksheet.append(data_list)
workbook.save(file_path)
```

```python
# 在某一区域内插入值
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
for row in worksheet['A1:B3']:
    for cell in row:
        cell.value = 'ning'
workbook.save(file_path)
```

## 八、行、列的插入与删除

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
# 插入列
worksheet.insert_cols(1, 2)  # 其中1指插入的位置，2指插入的行数
worksheet.insert_rows(1, 2)  # 其中1指插入的位置，2指插入的行数
worksheet.delete_cols(1, 2)  # 其中1指删除的位置，2指删除的行数
worksheet.delete_rows(1, 2)  # 其中1指删除的位置，2指删除的行数
workbook.save(file_path)
```

## 九、移动单元格

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
# "A1:C3"为需要移动的单元格，rows和cols正数为向下或向右、负数为向左或向上
worksheet.move_range("A1:C3", rows=10, cols=10)
workbook.save(file_path)
```

## 十、冻结单元格

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
worksheet.freeze_panes = "C3"
workbook.save(file_path)
```

## 阶段练习

### 求固定单元格数值和

```python
# 求固定区域数值和
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
list0 = []
for sheet in workbook.worksheets:
    list0.append(sheet['A1'].value)
print(sum(list0))
# 或者
print(sum(sheet['A1'].value for sheet in workbook.worksheets))
```

### 按行或者列求和

```python
# 按行求和
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
for row in list(worksheet.rows)[1:]:
    data_list = [cell.value for cell in row]
    print(sum(data_list))
```

```python
# 按列求和
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
for col in list(worksheet.columns)[1:]:
    data_list = [cell.value for cell in col]
    print(sum(data_list))
```

### 和大于30标记为优秀

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
for col in worksheet.iter_cols(min_row=1, min_col=2):
    data_list = [cell.value for cell in col[:-1]]
    print(sum(data_list))
    if sum(data_list) > 30:
        col[-1].value = '优秀'
workbook.save(file_path)
```

### 筛选和大于40的列

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
for row in range(worksheet.max_row, 0,-1):
    data_list =[cell.value for cell in worksheet[row]]
    if sum(data_list) <= 20:
        print(sum(data_list))
        worksheet.delete_rows(row)
workbook.save(file_path)
```

## 十一、合并与取消合并单元格

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
worksheet.merge_cells('B3:F5')  # 合并
worksheet.unmerge_cells('B3:F5')  # 取消合并
# worksheet.merge_cells(start_row=起始行号，start_column=起始列号,end_row=结束行号,end_column=结束列号) 
workbook.save(file_path)
```

## 十二、使用公式与注意事项

```python
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path)
worksheet = workbook['Sheet1']
worksheet['F1'] = '=sum(A1:E1)'
workbook.save(file_path)
```

```python
# 注意读取时会直接读取公式，所以要进行如下设置
import openpyxl as vb

file_path = r"C:\Users\zhou\Desktop\笔记\示例.xlsx"
workbook = vb.load_workbook(file_path, data_only=True)
worksheet = workbook['Sheet1']
print(worksheet['F1'].value)
```

[**关于"data_only"踩过的坑**](https://www.cnblogs.com/vhills/p/8327918.html )

