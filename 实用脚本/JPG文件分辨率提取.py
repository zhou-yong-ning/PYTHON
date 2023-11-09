from PIL import Image
import os
import pandas as pd

# 获取当前文件夹路径
Current_Folder_path = os.getcwd()
# 获取路径下的所有文件
file_list = os.listdir(Current_Folder_path)
file_list = [i for i in file_list if i.endswith('.jpg')]
DF = []
# 打开图片文件
for i in file_list:
    img = Image.open(i)
    # 获取图片分辨率
    width, height = img.size
    DF.append([i, width, height])

df = pd.DataFrame(DF, columns=['图片', '宽度', '高度'])
df.to_excel('文件分辨率提取.xlsx')