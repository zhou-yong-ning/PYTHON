# JSON文件提取

```python
def JSON(json_file):
    # 打开json文件
    f = open(json_file, 'r',encoding='utf-8')
    # 读取文件
    content = f.read()
    # 关闭文件
    f.close()
    # 字符串转字典
    a = json.loads(content)
    # 美化格式
    data = json.dumps(a, sort_keys=True, indent=4, separators=(',', ': '))
    print(data)
    return a
```

# TXT文件提取

```python
def TXT(txt_file):
    with open(file=txt_file, mode="r", encoding="utf-8") as f:
        data = f.read()
        print(data)
        print(type(data))
```

