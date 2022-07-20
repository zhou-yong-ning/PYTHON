# openpyxl日常练习

## 调整指定区域单元格格式

### 例一

```python
import os
import openpyxl as vb
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment

Current_Folder_path = os.getcwd()
# 遍历当前文件夹下的文件
file_list0 = os.listdir(Current_Folder_path)
# 推导式获取后缀为'.xlsx'的文件
file_list1 = [i for i in file_list0 if i.endswith('.xlsx')]
if not os.path.exists(Current_Folder_path + '\\NewFolder'):
    os.mkdir(os.path.join(Current_Folder_path, 'NewFolder'))
# 使用openpyxl打开文件
wb = vb.load_workbook(os.path.join(Current_Folder_path, file_list1[0]))
# 获取第一个工作表
ws = wb.worksheets[0]
# 获取最大行数
max_row = ws.max_row
# 获取单元格范围
ceel_range= ws['A2':f'M{max_row}']
# 循环调整单元格格式
for i in ceel_range:
    for j in i:
        j.alignment = Alignment(horizontal="center", vertical="center")
# 保存路径
wb.save(os.path.join(Current_Folder_path, 'NewFolder',file_list1[0]))
```

