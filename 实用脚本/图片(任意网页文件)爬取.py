import requests
from fake_useragent import UserAgent
import pandas as pd
import os

Current_Folder_path = os.getcwd()
if not os.path.exists(Current_Folder_path + '\\NewFolder'):
    os.mkdir(Current_Folder_path + '\\NewFolder')
file_list = os.listdir(Current_Folder_path)
excel_list = [a for a in file_list if a.endswith('.xlsx')]
rename_df = pd.read_excel(excel_list[0], dtype='object')
for i in rename_df.index.tolist():
    # pandas条件查询
    src_url = rename_df.loc[i, 'url']
    name = rename_df.loc[i, 'name']
    src_headers = {
        'User-Agent': UserAgent().chrome
    }
    src_resp = requests.get(url=src_url, headers=src_headers).content
    with open('./NewFolder/' + name, 'wb') as f:
        f.write(src_resp)
    print(name + '下载成功')
