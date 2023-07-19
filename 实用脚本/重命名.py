import os

# 获取当前.py文件所在绝对路径
Current_Folder_path = os.getcwd()
# 获取指定文件夹内所有文件
file_list = os.listdir(Current_Folder_path)
# 利用推导式获取所有后缀不为”.py“和“.idea”的文件
file_list1 = [a for a in file_list if not a.endswith('.py') and a != '.idea']
for i in file_list1:
    # 替换文档内任意值
    newname = i.replace('.', '中心线.', 1)
    # (旧文件名路径，新文件名路径)
    os.rename(os.path.join(Current_Folder_path, i), os.path.join(Current_Folder_path, newname))
