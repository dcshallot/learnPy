
## 学习进行中，调用时需要在命令行下在安装目录启动Python，并将文件放在同目录

from numpy import *  # 导入科学计算模块
import operator # 导入运算符模块
	
def classify0 ( inX, dataSet, labels, k ) :
	# 计算新向量和每一个训练样本之间的欧氏距离
	dataSetSize = dataSet.shape[0]  # shape返回数据的形状[0]应该是第一个维度，训练样本Nrow
	diffMat = tile( inX, (dataSetSize,1)) - dataSet  # tile相当于rep，整个句子计算x-y
	sqDiffMat = diffMat**2 # ( x-y )^2，矩阵
	sqDistances = sqDiffMat.sum( axis = 1) # 求和
	distances = sqDistances**0.5 # 开平方，得到欧氏距离
	# 按照距离远近排序并选择最近的k个点
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[ sortedDistIndicies[i]]
		classCount[ voteIlabel] = classCount.get( voteIlabel,0 ) + 1
	sortedClassCount = sorted( classCount.iteritems(),
		key = operator.itemgetter(1), reverse =True )
	return sortedClassCount[0][0]
	 
'''
def createDataSet():
	group = array( [[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels
	
group, labels = createDataSet() #创建训练集 
a = classify0( [0,0], group , labels, 3)
print a
'''

# 从文本中解析数据
def file2matrix( filename):
	fr = open(filename)
	arrayOfLines = fr.readlines()
	numberOfLines = len( arrayOfLines ) # nrow
	returnMat = zeros(( numberOfLines, 7 )) # 生成一个空矩阵
	classLabelVector = [] 
	index = 0
	for line in arrayOfLines:
		line = line.strip() # 去掉所有回车
		listFromLine = line.split(',') # 每行分隔符
		returnMat[ index, :] = listFromLine[ 0: 7 ] # 
		classLabelVector.append( int(listFromLine[-1])) # 最后1列为Y
		index += 1
	return returnMat, classLabelVector

# 归一化数据
def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals, (m,1))
	normDataSet = normDataSet/tile( ranges, (m,1))
	return normDataSet, ranges, minVals

# 归一回头再说！！！
datingDataMat, datingLabels = file2matrix( 'C:/Users/dingchong/Documents/GitHub/learnPy/train.csv')

import pandas as pd
data = pd.DataFrame(datingDataMat)

pred = classify0( datingDataMat, datingDataMat , datingLabels, 3) 

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter( datingDataMat[:,3], datingDataMat[:,4], 15*array(datingLabels), 15*array(datingLabels))
plt.show()









