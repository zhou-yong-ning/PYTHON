import pandas as pd
import os
# 获取当前文件夹路径
Current_Folder_path = os.getcwd()
# 建立数据表
concat_df = pd.DataFrame()
# 获取路径下的所有文件
file_list = os.listdir(Current_Folder_path)
# 提取后缀为‘.xlsx’的文件
file_xlsx = [i for i in file_list if i.endswith('.xlsx')]
# 遍历列表中的文件
for file_name in file_xlsx:
    try:
        print('正在合并',file_name)
        df = pd.read_excel(os.path.join(Current_Folder_path,file_name),dtype='object')
        df['文件名'] = file_name
        # 合并
        concat_df =pd.concat([concat_df,df])
    except:
        print(file_name,'发生异常')
        continue
print('正在写入中......')
concat_df.to_excel(os.path.join(Current_Folder_path,'合并表.xlsx'),index=False)
# concat_df.to_csv(os.path.join(Current_Folder_path, '合并表.txt'), sep='\t', encoding='ANSI',index=False)  # 制表符分隔
# concat_df.to_csv(os.path.join(Current_Folder_path, '合并表.txt'), sep=',', encoding='ANSI',index=False)  # 逗号分隔
print('写入完成')
