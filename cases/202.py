# 输出乘法口诀表 
'''
输入1个整数n，输出n * n的乘法口诀表。用制表符分隔。
'''

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
