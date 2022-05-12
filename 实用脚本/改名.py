import os

_path = "E:\\行政勘界\\市级核查整改图\\20220511（扫描件）\\20220512"  #指定文件路径为
path = os.listdir(_path)                    #读取路径中的文件名，导出到列表
jpg_ = [x for x in path if x.endswith(".jpg")]    #读取后缀为“.*”的文件名
print(jpg_)
for i in jpg_:
    newname = i.split('.')[0]+'村级管理线成果图.jpg'
    print(newname)
    os.rename(_path + "\\" + i,_path + "\\" + newname)