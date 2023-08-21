# 导入pdf2docx模块
from pdf2docx import Converter
import os


def pdf2word(pdf_path, docx_file):
    # 创建Converter对象
    p2w = Converter(pdf_path)
    # 执行转换方法，start开始页，0从第一页开始，end结束页，None为无限制
    p2w.convert(docx_file, start=0, end=None)
    p2w.close()


# 获取当前文件夹路径
Current_Folder_path = os.getcwd()
if not os.path.exists(Current_Folder_path + '\\NewFolder'):
    os.mkdir(os.path.join(Current_Folder_path, 'NewFolder'))
pdfpath = os.path.join(Current_Folder_path, 'NewFolder')
# 获取路径下的所有文件
file_list = os.listdir(Current_Folder_path)
# 提取后缀为‘.pdf’的文件
pdf_files = [i for i in file_list if i.endswith('.pdf')]
for i in pdf_files:
    # 指定输出路径
    output_file = os.path.join(Current_Folder_path, 'NewFolder', i.split('.')[0] + '.docx')
    # 调用方法
    pdf2word(i, output_file)
