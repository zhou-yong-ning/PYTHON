## 1.批量去除文件名中的括号：

```bat
@Echo Off&SetLocal ENABLEDELAYEDEXPANSION
FOR %%a in (*) do (
    echo 正在处理 %%a
    set "name=%%a"
    set "name=!name:(=!"
    set "name=!name:)=!"
    ren "%%a" "!name!"
)
exit
```

## 2.批量去除文件名中的空格：

```bat
@echo off&setlocal enabledelayedexpansion
for /f "delims=" %%i in ('dir /s/b *.*') do (
    set "foo=%%~nxi"
    set foo=!foo: =!
    set foo=!foo: =!
    ren "%%~fi" "!foo!"
)
exit
```

## 3.批量重命名：

```bat
ren	旧.后缀	新.后缀
ren	旧.jpg	新.jpg
ren	旧.docx	新.docx
```

## 4.删除文件

删除当前目录下的test.txt文件

```bat
del test.txt
```

删除上级目录下的test.txt文件

```bat
del ..\test.txt
```

删除当前目录TEST文件夹下的所有.o文件

```bat
del .\TEST\*.o
```

## 5.复制文件：支持多个文件操作，同时支持上级及下级文件路径

```bat
copy file1.txt 文件夹1
copy file2.txt 文件夹2
```

## 6.移动文件与文件夹：支持多个文件操作，同时支持上级及下级文件路径

```Bat
move 文件夹1 文件夹2
move file2.txt 文件夹2
```

## 7.创建文件夹

```bat
md 文件夹
```

## 8.当前目录创建a.txt文件

```bat
cd.>a.txt
```

## 9.提取文件名

提取当前目录下扩展名为mp3的文件名，输出到`mp3文件名.txt`

```bat
dir *.mp3 /b>mp3文件名.txt
```

提取当前目录下的“深度睡眠”文件夹下的所有mp3文件名到文件

```bat
dir .\深度睡眠\*.mp3 /b>mp3文件名.txt
```

提取当前目录下所有文件的文件名到a.txt

```bat
dir c:\*.* >a.txt
```
提取当前目录以及子目录下的文件夹名

```bat
dir/a/s/b>LIST.xlsx
```
