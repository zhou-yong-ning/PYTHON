# pandas100题练习

```python
import pandas as pd
import numpy as np

data = {"grammer": ["Python", "C", "Java", "GO", np.nan, "SQL", "PHP", "Python"],
        "score": [1, 2, np.nan, 4, 5, 6, 7, 10]}
df = pd.DataFrame(data)
```



## 1.提取含有字符串"Python"的行

```python
# 方法一
a = df[df['grammer'] == 'Python']
print(a)
# 方法二
results = df['grammer'].str.contains("Python")
results.fillna(value=False, inplace=True)
print(df[results])
```

## 2.输出df的所有列名

```python
print(df.columns)
# 相当于一个列表
```

## 3.修改第二列列名为'popularity'

```python
df.rename(columns={'score':'popularity'}, inplace = True) #可以同时修改多个列表名
```

## 4.统计grammer列中每种编程语言出现的次数

```python
df1 = df['grammer'].value_counts()
# 查看‘C’数量
print(df1['C'])
```

## 5.将空值用上下值的平均值填充

```python
df['popularity'] = df['popularity'].fillna(df['popularity'].interpolate())
print(df)
```

## 6.提取popularity列中值大于3的行

```python
df1 = df[df['popularity'] > 3]
print(df1)
```

## 7.按照grammer列进行去除重复值

```python
df1 = df.drop_duplicates(['grammer'])
print(df1)
```

## 8.计算popularity列平均值

```python
df1 = df['popularity'].mean()
print(df1)
```

## 9.将grammer列转换为list

```python
df1 = df['grammer'].tolist()
print(df1)
```

## 10.查看数据行列数

```python
df1 = df.shape # 返回一个元组
print(df1)
```

## 11.提取popularity列值大于3小于7的行

```python
df1 = df[(df['popularity'] > 3) & (df['popularity'] < 7)] # 不能用and
print(df1)
```

## 12.交换两列位置

```python
# 方法1
temp = df['popularity']
df.drop(labels=['popularity'], axis=1, inplace=True)
df.insert(0, 'popularity', temp)
print(df)

# 方法2
# cols = df.columns[[1,0]]
# df = df[cols]
# print(df)
```

