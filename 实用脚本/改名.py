import os

# 获取当前.py文件所在绝对路径
Current_Folder_path = os.getcwd()
# 获取指定文件夹内所有文件
file_list = os.listdir(Current_Folder_path)
# 利用推导式获取所有后缀为”.doc“的文件
docx_list = [a for a in file_list if a.endswith('.docx')]
for i in docx_list:
    newname = i.split('.')[0] + "修改.docx"
    # newname = newname.replace("改","") + '.docx'
    print(newname)
    os.rename(Current_Folder_path + "\\" + i, Current_Folder_path + "\\" + newname)  # (旧文件名路径，新文件名路径)
