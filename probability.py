# 网易公开课——概率论与数理统计
# 第一章

'''
蒙提霍尔问题：
3扇门里有1汽车2山羊，玩家选其一，主持人打开另两扇门里有山羊的那道门
问，玩家换门还是不换门的中奖概率大
'''
import random
# 输入参赛者选择的门（1-3），是否改变选择
def MontyHall( Dselect, Dchange):
	Dcar=random.randint(1,3)
	if Dcar == Dselect and Dchange == 0:
		return 1
	elif Dcar != Dselect and Dchange == 0:
		return 0 
	elif Dcar == Dselect and Dchange ==1:
		return 0
	else:
		return 1

# 模拟中奖概率
n = 10000
# 换与不换随机选 0.5
win = 0
for i in range(n):
	Dselect=random.randint(1,3)
	Dchange=random.randint(0,1)
	win=win+MontyHall(Dselect, Dchange)
print float(win)/float(n)

# 坚决不换 0.3
win = 0
for i in range(n):
	Dselect=random.randint(1,3)
	Dchange=0
	win=win+MontyHall(Dselect, Dchange)
print float(win)/float(n)

# 坚决换 0.66
win = 0
for i in range(n):
	Dselect=random.randint(1,3)
	Dchange=1
	win=win+MontyHall(Dselect, Dchange)
print float(win)/float(n)


'''
求圆周率——蒙特卡洛方法
'''
import random
n=100000
k=0
for i in range(n):
	x=random.uniform(-1,1)
	y=random.uniform(-1,1)
	if x**2+y**2<1:
		k=k+1
print 4*float(k)/float(n)




