# 华氏温度转换为摄氏温度 
'''
输入1个整数华氏温度，输出摄氏温度。华氏温度到摄氏温度的转换公式为：C=(F
- 32) / 1.8。
'''

f = int(input())
c = (f - 32) / 1.8
print('%.2f' % c)

