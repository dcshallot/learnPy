# 网易公开课——概率论与数理统计
# 第二章 随机变量及其分布

'''
概率实现
离散分布：二项，几何，泊松
连续分布：均匀，指数，正态
'''

# 二项
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom as B 

rv = B(10, 0.5)
x = np.arange( 0, 11, 1 )
y = rv.pmf(x)

print y
plt.bar(x, y , width = 0.6, color = 'grey')
plt.show()

# 几何
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom as G 

rv = G( 0.2 )
x = np.arange( 1, 11, 1 )
y = rv.pmf(x)

print y
plt.bar(x, y, width = 0.6, color = 'grey')
plt.show()


# 正态
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm as N

x = np.linspace( -10, 10, 100 )
rv1 = N( loc =0, scale =1)
rv2 = N( loc=-5, scale =1)
rv3 = N( loc=0, scale=3)

plt.plot( x, rv1.pdf(x), color = 'green' )
plt.plot( x, rv2.pdf(x), color = 'green' )
plt.plot( x, rv3.pdf(x), color = 'green' )
plt.show()


# 指数分布
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon as E

rv1 = E( scale =1.5)
rv2 = E( scale =1.0)
rv3 = E( scale =0.5)

x = np.linspace(0, 20, 100 )
plt.plot( x, rv1.pdf(x), color = 'green' )
plt.plot( x, rv2.pdf(x), color = 'blue' )
plt.plot( x, rv3.pdf(x), color = 'red' )
plt.show()



# 生成随机分布的数据
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon as E 

def exp(lam):
	p = random.random()
	return - math.log(1-p)/lam
x1 = []
for i in range(100):
	x1.append(exp(1))
x1 = sorted(x1)
y1 = np.linspace( 0, 1, 100)
plt.plot( x1, y1, color = 'blue')

rv = E(scale =1)
x2 = np.linspace( 0, 5, 100)
plt.plot( x2, rv.cdf(x2), color = 'red' )
plt.show()







