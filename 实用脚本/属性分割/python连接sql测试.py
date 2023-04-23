import pandas as pd
import pymysql
import warnings

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 忽略警告
    warnings.filterwarnings('ignore')
    # 创建连接对象
    conn = pymysql.connect(host='localhost', user='root', password='zyn19991127', port=3306,database='zg', charset='utf8')
    # 创建查询语句
    sql = "select * from ncjtjjzzzong"
    # 读取数据表
    df = pd.read_sql_query(sql=sql, con=conn)
    print(df)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

# sqlite3数据库连接测试
import sqlite3
import pandas as pd

# 直接在当前文件夹内创建数据库
conn = sqlite3.connect('test.db')
# 指定sql查询语句
sql = "select * from ncjtjjzzzong"
# 读取数据表
df = pd.read_sql_query(sql=sql, con=conn)
print(df)
