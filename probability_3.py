# 网易公开课——概率论与数理统计
# 第三章 二维随机变量

'''
三维作图
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np 

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
for c,z in zip(['r','g','b','y'],[30,20,10,0]):
	x = np.arange(20)
	y = np.random.rand(20)
	c = [c]*len(x)
	ax.bar(x,y,z,zdir ='y', color=c) # 3d柱状图

plt.show()