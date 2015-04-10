
'''
美股资金规模最优值估算
设定：CYOU股价在26美元之间波动，低买高卖的价差在0.8-0.6美元之间
费用规则按富途收取
'''

import random
pbuy = 26
psell = pbuy + random.uniform(0.6,0.8) 
n = 500
buy = - pbuy * n - max(0.003*n, 3) - 5 
sell = psell * n - max(0.003*n, 3) - 5 - (0.000021 * psell * n) - ( 0.000119 * n)

print psell
print n
print (sell + buy)
