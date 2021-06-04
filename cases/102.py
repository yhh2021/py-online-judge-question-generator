# 检查能否构成三角形 
'''
输入3个整数边长，输出结果
'''

a, b, c = map(int, input().split())
print(a + b > c and a + c > b and b + c > a)
