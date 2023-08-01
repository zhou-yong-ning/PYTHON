from pdf2image import convert_from_path
import os


def pdf_to_jpg(pdf_path, output_folder):
    name = pdf_path.split('.')[0]
    # 将PDF转换为图像
    images = convert_from_path(pdf_path)
    # 循环将pdf中每个图像保存为JPG文件
    for i, image in enumerate(images):
        # 图片编号
        bh = ''.join(['(', str(i + 1), ')'])
        # 设置路径
        image_path = os.path.join(output_folder, '.'.join([name + bh, 'jpg']))
        # 保存
        image.save(image_path, "JPEG")
        print(name + bh)


# 获取当前.py文件所在绝对路径
Current_Folder_path = os.getcwd()
# 获取指定文件夹内所有文件
file_list = os.listdir(Current_Folder_path)
# 利用推导式获取所有后缀为”.pdf“
file_list1 = [a for a in file_list if a.endswith('.pdf')]
# 创建文件夹
if not os.path.exists('NewFolder'):
    os.mkdir(os.path.join('NewFolder'))
# 输出文件夹路径
output_folder = "NewFolder"
for i in file_list1:
    try:
        pdf_to_jpg(i, output_folder)
    except:
        print(i,'转换失败')
input('按任意键结束:')