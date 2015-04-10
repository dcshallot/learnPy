'''
linux下环境配置
记得先sodu apt-get update/upgrade一下！
'''


apt-get install python-pip
# 先尝试安装pip,done

pip install numpy
# 出错
sudo apt-get install python-numpy
# 绕行安装numpy，done
apt-get install python-scipy
# done

'''
matplotlib安装比较麻烦，参考
http://my.oschina.net/u/939893/blog/163921

'''

# 慢的解决方法: 使用镜像的方法可以在每次执行pip的时候加上参数"-i国内镜像"即可
pip install -i http://pypi.douban.com/simple matplotlib

