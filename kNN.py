
## 学习进行中，调用时需要在命令行下在安装目录启动Python，并将文件放在同目录

from numpy import *  # 导入科学计算模块
import operator # 导入运算符模块

def createDataSet():
	group = array( [[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels
	
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
	 

	 
	 