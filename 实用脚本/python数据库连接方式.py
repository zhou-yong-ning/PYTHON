import pandas as pd

# 指定路径和匹配字段匹配方式
path1 = r"E:\宅基地改革数据\农业局乱占耕地\一标段数据提取\国土空间挂接.xlsx"
path2 = r"C:\Users\zhou\Desktop\pyceshi\使用权人表数据 (75).xlsx"
path0 = r"C:\Users\zhou\Desktop\pyceshi\合并表.xlsx"
ziduan = '宅基地代码'
how = 'left'

df1 = pd.read_excel(path1)
df2 = pd.read_excel(path2)
df0 = pd.merge(df1, df2, on=ziduan, how=how)
df0.to_excel(path0, index=None)
