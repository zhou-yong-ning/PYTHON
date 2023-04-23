import pandas as pd
import os
from multiprocessing import Process
import sqlite3

def dxcfor(dfbiao, list, col):
    Current_Folder_path = os.getcwd()
    for i in list:
        i = str(i)
        df0 = dfbiao.loc[(dfbiao[col] == i)]
        # 根据指定列进行升排序
        # df0.sort_values(by=['承包方编码'], ascending=True, inplace=True)
        df0.to_excel(os.path.join(Current_Folder_path, 'NewFolder', i + '.xlsx'), index=False)
        print(i + ' 表格导出成功')


if __name__ == '__main__':
    Current_Folder_path = os.getcwd()
    # 遍历当前文件夹下的文件
    file_list0 = os.listdir(Current_Folder_path)
    if not os.path.exists(Current_Folder_path + '\\NewFolder'):
        os.mkdir(os.path.join(Current_Folder_path, 'NewFolder'))

    # 指定分割列名称
    col = '村'
    # 直接在当前文件夹内创建数据库
    conn = sqlite3.connect('TEST.db')
    # 指定sql查询语句
    sql = "select * from FDYTHNCY"
    # 读取数据表
    df = pd.read_sql_query(sql=sql, con=conn)
    # 打印数据表
    print(df)

    # 获取某一列唯一值
    listType = df[col].unique()
    print(listType)
    # 多进程循环筛选导出
    Processnum = 6  # 指定进程数
    listnum = len(listType) // Processnum + 1  # 计算每个进程任务
    Arr = []
    for j in range(0, len(listType), listnum):
        if j + listnum <= len(listType):
            p = Process(target=dxcfor, args=(df, listType[j:j + listnum], col))
            p.start()
            print(p,"进程开始")
            Arr.append(p)
        else:
            p = Process(target=dxcfor, args=(df, listType[j:len(listType) + 1], col))
            p.start()
            print(p,"进程开始")
            Arr.append(p)
    for k in Arr:
        k.join()
    print('分表完成')
