# 计算圆的周长和面积
'''
输入1个整数半径，输出保留两位小数的周长和面积。
'''

radius = int(input())
perimeter = 2 * 3.1415926535 * radius
area = 3.1415926535 * radius * radius
print('%.2f' % perimeter)
print('%.2f' % area)
