import pandas as pd
import os



# 获取当前文件夹路径
Current_Folder_path = os.getcwd()
# 创建文件夹
if not os.path.exists(Current_Folder_path + '\\NewFolder'):
    os.mkdir(Current_Folder_path + '\\NewFolder')
# 遍历当前文件夹下的文件
file_list = os.listdir(Current_Folder_path)
# 提取后缀为xls的文件
xlsx_list = [a for a in file_list if a.endswith('.xlsx')]
for i in xlsx_list:
    try:
        data = pd.read_excel(i,header=3,index_col=0,dtype='object')
        data['身份证号码'] = data['身份证号码']+data['民族']
        j = i.split('.')[0] + '.csv'
        data.to_csv(os.path.join(Current_Folder_path,'NewFolder',j),encoding='UTF-8')
    except:
        print(i)
        continue
