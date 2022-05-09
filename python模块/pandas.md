# pandas

## 1.读取数据

### 1.1读取CSV，使用默认的标题行、逗号分隔符

```python
import pandas as pd
```

```python
# 使用pd.read_csv读取数据
ratings = pd.read_csv(fpath)
# 查看数据的形状，返回(行数、列数)
ratings.shape
# 查看列名列表
ratings.columns
# 查看索引列
ratings.index
# 查看每列的数据类型
ratings.dtypes
```

### 1.2 读取txt文件，自己指定分隔符、列名

```python
pvuv = pd.read_csv(
    fpath,
    sep="\t",
    header=None,
    names=['pdate', 'pv', 'uv']
)
```

### 1.3、读取excel文件

```python
pvuv = pd.read_excel(fpath)
```

### 1.4、读取MySQL数据库

```python
import pymysql
conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='12345678',
        database='test',
        charset='utf8'
    )
mysql_page = pd.read_sql("select * from crazyant_pvuv", con=conn)
```

## 2.数据结构

### 2.1. Series

**Series是一种类似于一维数组的对象，它由一组数据（不同数据类型）以及一组与之相关的数据标签（即索引）组成。**

```python
import pandas as pd
```

```python
s1 = pd.Series([1,'a',5.2,7])
# 左侧为索引，右侧是数据
s1
# 获取索引(索引默认从零开始)
s1.index
# 获取数据
s1.values
```

#### 2.1.1 创建一个具有标签索引的Series

```python
s2 = pd.Series([1, 'a', 5.2, 7], index=['d','b','a','c'])
```

#### 2.1.2 使用Python字典创建Series

```python
sdata={'Ohio':35000,'Texas':72000,'Oregon':16000,'Utah':5000}
s3=pd.Series(sdata)
# 索引为字典的key
```

#### 2.1.3根据标签索引查询数据

**类似Python的字典dict**

### 2.2. DataFrame

**DataFrame是一个表格型的数据结构**

**每列可以是不同的值类型（数值、字符串、布尔值等）**

**既有行索引index,也有列索引columns**

**可以被看做由Series组成的字典**

#### 2.2.1 根据多个字典序列创建dataframe

```python
data={
        'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]
    }
df = pd.DataFrame(data)
```

### 2.3从DataFrame中查询出Series

**如果只查询一行、一列，返回的是pd.Series**

**如果查询多行、多列，返回的是pd.DataFrame**

**查询一列，结果是一个pd.Series**

```
df['year']
type(df['year'])
```

**查询多列，结果是一个pd.DataFrame**

```python
df[['year', 'pop']]
type(df.loc[1])
```

**查询多行，结果是一个pd.DataFrame**

```python
df.loc[1:3]
type(df.loc[1:3])
```

## 数据查询

**## Pandas查询数据的几种方法**

1. df.loc方法，根据行、列的标签值查询

2. df.iloc方法，根据行、列的数字位置查询

3. df.where方法

4. df.query方法

.loc既能查询，又能覆盖写入，强烈推荐！

**## Pandas使用df.loc查询数据的方法**

1. 使用单个label值查询数据

2. 使用值列表批量查询

3. 使用数值区间进行范围查询

4. 使用条件表达式查询

5. 调用函数查询

**## 注意**

\* 以上查询方法，既适用于行，也适用于列

\* 注意观察降维dataFrame>Series>值

```python

```

