'''
网易公开课——疯狂的python
章节6高级功能
课时32文件读写21:50
课时33文件对象的方法18:57
课时34Os模块15:34
课时35目录遍历27:48
课时36异常处理25:36
课时37MySQL数据库模块
课时38面向对象编程之类和对象
'''

## 文件与目录

# 目录分析器
# 杀毒软件
# 系统垃圾清理工具


# 读写文件的函数是Open或者file类,获取句柄
fo = open( 'C:/Users/dingchong/Documents/GitHub/learnPy/predict2015-03-30.csv') 
fo.read() #
fo.close()

# 写数据
f1 = open('C:/Users/dingchong/Documents/GitHub/learnPy/test.txt', 'w')
f1.write('hello world \ni am new\have a nice day')
f1.close()

# open的方式
# r只读，r+读写,注意指针位置不同
# w写入，先删除后写入，如果没文件则创建
# w+读写
# a在末尾追加
# a+读写
# b二进制打开
# U支持所有换行符


# 可以用for循环 逐行open遍历文件内容
for i in open('C:/Users/dingchong/Documents/GitHub/learnPy/predict2015-03-30.csv'):
	print i 

# readline([size]) 每次读一行，每次读取size个字节直到行末
f1 = open('C:/Users/dingchong/Documents/GitHub/learnPy/predict2015-03-30.csv')
out = f1.readline()
print out
# 每次执行readline(), 读取open对象的下一行，可以理解为指针加一
out = f1.readline()
print out
out = f1.readline()
print out

# readlines 返回一个列表，每一行作为列表的元素
f1 = open('C:/Users/dingchong/Documents/GitHub/learnPy/predict2015-03-30.csv')
out = f1.readlines()
print out

# 对open对象的其他函数
# next类似readline但是会根据数据的行数停止，而非无休止的读取空值
# write 和 writelines 写入前是否清除原来数据，取决于open的方式
# seek( 偏移量，选项) 读取的位置指针
# flush 文件写入的提交更新


# 文件查找和替换
# 例子1统计文件中.com的个数
import re
f1 = open('C:/Users/dingchong/Documents/GitHub/learnPy/predict2015-03-30.csv')
count = 0 
for s in f1.readlines():
	li = re.findall("com",s )
	if len(li) > 0:
		count = count + len(li)
print count
f1.close()

# 把文件1中的.com替换为@mail，保存到change.csv中
import re
f1 = open('C:/Users/dingchong/Documents/GitHub/learnPy/predict2015-03-30.csv')
f2 = open('C:/Users/dingchong/Documents/GitHub/learnPy/change.csv', 'w')

for s in f1.readlines():
	f2.write( s.replace(".com", "@mail"))
f1.close()
f2.close()

# OS 模块——系统操作命令

import os
# 创建目录
os.mkdir('C:/Users/dingchong/Documents/GitHub/learnPy/jpg')

# mkdir, makedirs( names, mode = 511)
# rmdir(path) 移除目录
# removedirs(path) 删除彻底一点
# listdir(path) 显示路径下文件名
# getcwd() 类似pwd
# chdir(path) 
# walk( top, topdown = True, oneror =None))


 






