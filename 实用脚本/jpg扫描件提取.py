from PIL import Image
import pytesseract
import os
import pandas as pd

def extract_text_from_image(image_path):
    # 打开图像文件
    image = Image.open(image_path)
    # 使用Pytesseract提取文字
    extracted_text = pytesseract.image_to_string(image,lang='chi_sim')
    return [extracted_text]

def LIST_Processing(jpglist):
    DF0 = []
    for jpg_file in jpglist:
        # 调用pdf数据读取函数
        try:
            jpg = extract_text_from_image(jpg_file)
        except:
            jpg = '提取失败'
        # 单个列表中插入文件名
        jpg.insert(0, jpg_file)
        # 添加子列表
        DF0.append(jpg)
        print(jpg)
    return DF0


Current_Folder_path = os.getcwd()
if not os.path.exists(Current_Folder_path + '\\NewFolder'):
    os.mkdir(Current_Folder_path + '\\NewFolder')
# 遍历当前文件夹下的文件
file_list0 = os.listdir(Current_Folder_path)
# 提取后缀为jpg的文件
file_list = os.listdir(Current_Folder_path)
jpg_list = [a for a in file_list if a.endswith('.jpg')]
# 循环提取列表中的图片
DF = LIST_Processing(jpg_list)
df = pd.DataFrame(DF,columns=['文件名','图斑编号'])
df.to_excel(os.path.join(Current_Folder_path,'NewFolder\\文件提取.xlsx'))

