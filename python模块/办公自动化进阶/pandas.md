# 读取数据

## 读取txt与csv文件

| **数据类型**      | **说明**         | **读取方法**      |
| ----------------- | ---------------- | ----------------- |
| **csv、tsv、txt** | **默认逗号分隔** | **pd.read_csv**   |
| **csv、tsv、txt** | **默认\t分隔**   | **pd.read_table** |

**体验两种方法的区别，与sep指定分隔符**

**切记：如果分隔符不止一种，使用正则表达式sep='\s+'**

### 读取csv文件

```python
import pandas as pd

# file_path = r"C:\Users\zhou\Desktop\pandas\FBF.xlsx"
file_path = r"C:\Users\zhou\Desktop\pandas\FBF.csv"
df = pd.read_csv(file_path,encoding='ANSI', dtype='object')
# 打印数据
print(df)
# 打印前几行
print(df.head())
# 查看数据的形状，返回（行数、列数）
print(df.shape)
# 查看列名列表
print(df.columns)
# 查看索引列
print(df.index)
# 查看每一列数据类型
print(df.dtypes)
```

### **自己制定分隔符、列名**

```python
import pandas as pd

# file_path = r"C:\Users\zhou\Desktop\pandas\FBF.xlsx"
file_path = r"C:\Users\zhou\Desktop\pandas\FBF.csv"
df = pd.read_csv(file_path, sep=',', header=None, names=['姓名', '年龄', '地址', '电话', '入职日期'], encoding='ANSI', index_col='姓名')
print(df)
```

| **参数**      | **描述**                                                     |
| ------------- | ------------------------------------------------------------ |
| **sep**       | **分隔符或正则表达式 sep='\s+'**                             |
| **header**    | **列名的行号，默认0（第一行），如果没有列名应该为None**      |
| **names**     | **列名，与header=None一起使用**                              |
| **index_col** | **索引的列号或列名，可以是一个单一的名称或数字，也可以是一个分层索引** |
| **skiprows**  | **从文件开始处，需要跳过的行数或行号列表**                   |
| **encoding**  | **文本编码，例如utf-8**                                      |
| **nrows**     | **从文件开头处读入的行数**  **nrows=3**                      |

# to_excel详细参数

```python
# to_excel方法定义：

DataFrame.to_excel(path, 
                   sheet_name='Sheet1',
                   na_rep='',
                   float_format=None, 
                   columns=None, 
                   header=True, 
                   index=True, 	     
                   index_label=None, 
                   startrow=0, 
                   startcol=0, 
                   engine=None, 
                   merge_cells=True, 
                   encoding=None, 
                   inf_rep='inf', 
                   verbose=True, 
                   freeze_panes=None)
```

**path: 字符串或ExcelWriter 对象，文件路径或现有的ExcelWriter**

**sheet_name :字符串,默认“Sheet1”，将包含DataFrame的表的名称。**

**na_rep : 字符串,默认‘ ’缺失数据表示方式**

**float_format : 字符串,默认None，格式化浮点数的字符串**

**columns : 序列,可选，要编写的列**

**header : 布尔或字符串列表，默认为Ture。写出列名。如果给定字符串列表，则假定它是列名称的别名。**

**index :布尔,默认的Ture写行名（索引）**

**index_label : 字符串或序列，默认为None。如果需要，可以使用索引列的列标签。如果没有给出，标题和索引为true，则使用索引名称。如果数据文件使用多索引，则需使用序列。**

**startrow :左上角的单元格行来转储数据框**

**startcol :左上角的单元格列转储数据帧**

**engine : 字符串,默认没有使用写引擎 - 您也可以通过选项io.excel.xlsx.writer，io.excel.xls.writer和io.excel.xlsm.writer进行设置。**

**merge_cells : 布尔,默认为Ture编码生成的excel文件。 只有xlwt需要，其他编写者本地支持unicode。**

**inf_rep : 字符串,默认“正”无穷大的表示(在Excel中不存在无穷大的本地表示)**

**freeze_panes : 整数的元组(长度2)，默认为None。**

# **read_excel**详细参数

pandas.read_excel接口用于读取excel格式数据文件，由于它使用非常频繁，功能强大参数众多，

所以在这里专门做详细介绍，我们在使用过程中可以查阅。

## 语法

```python
import pandas as pd

pd.read_excel(path, 
              sheet_name=0，
              header=0,
              names=None,
              index_col=None,
              usecols=None,
              squeeze=False,
              dtype=None,
              engine=None,
              converters=None，
              true_values=None,
              false_values=None，
              skiprows=None,
              nrows=None,
              na_values=None,
              keep_default_na=True，
              verbose=False,
              parse_dates=False， 
              date_parser=None,
              thousands=None，
              comment=None,
              skipfooter=0,
              convert_float=True，
              mangle_dupe_cols=True，
              **kwds)
```

### sheet_name

```python
pd.read_excel( 'tmp.xlsx' , sheet_name=1) #第二个sheet
pd.read_excel( 'tmp.xlsx', sheet_name= '总结表') #按sheet的名字
#取第一个、第二个、名为Sheet5 的，返回一个df组成的字典
dfs = pd.read_excel('tmp.xlsx',sheet_name=[0，1，"Sheet5"])
dfs = pd.read_excel('tmp.xlsx', sheet_name=None） #所有的sheetdfs [ "Sheet5' ]#读取时按sheet名
```

### header

```python
pd .read_excel( 'tmp.xlsx', header=None)#不设表头
pd.read_excel( 'tmp.xlsx ', header=2)#第三行为表头
pd.read_excel( 'tmp.xlsx' , header=[0，1])#两层表头，多层索引
```

