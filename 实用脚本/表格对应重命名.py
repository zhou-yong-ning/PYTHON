import os
import pandas as pd

rename_df = pd.read_excel('rename.xlsx', dtype='object')
for i in rename_df.index.tolist():
    # pandas条件查询
    old_name = rename_df.loc[i, '旧']
    new_name = rename_df.loc[i, '新']
    # (旧文件名路径，新文件名路径)
    os.rename(old_name, new_name)
