import pandas as pd
import openpyxl
import os
# 获取当前文件夹路径
Current_Folder_path = os.getcwd()
# 建立数据表
concat_df = pd.DataFrame()
# 获取路径下的所有文件
file_list = os.listdir(Current_Folder_path)
# 提取后缀为‘.xlsx’的文件
file_xlsx = [i for i in file_list if i.endswith('.xlsx')]
# 指定第一个工作簿文件
xlsx_path = file_xlsx[0]
# 读取工作簿
print('正在读取')
workbook = openpyxl.load_workbook(os.path.join(Current_Folder_path,xlsx_path))
print('读取完成')
# 循环读取工作表
for work_sheet in workbook.sheetnames:
    # 循环调用调整表格格式函数
    print(work_sheet)
    try:
        print('正在合并',work_sheet)
        df = pd.read_excel(os.path.join(Current_Folder_path,xlsx_path),sheet_name=work_sheet,dtype='object',header=None)
        # 合并
        concat_df =pd.concat([concat_df,df])
    except:
        print((work_sheet,'发生异常'))
        continue
print('正在写入中......')
concat_df.to_excel(os.path.join(Current_Folder_path,'合并表.xlsx'),index=False)
print('写入完成')
