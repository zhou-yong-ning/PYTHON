# 一、读取数据

## 1、读取txt与csv文件

| **数据类型**      | **说明**         | **读取方法**      |
| ----------------- | ---------------- | ----------------- |
| **csv、tsv、txt** | **默认逗号分隔** | **pd.read_csv**   |
| **csv、tsv、txt** | **默认\t分隔**   | **pd.read_table** |

**体验两种方法的区别，与sep指定分隔符**

**切记：如果分隔符不止一种，使用正则表达式sep='\s+'**

### 1.1读取csv文件

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

### 1.2**自己制定分隔符、列名**

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