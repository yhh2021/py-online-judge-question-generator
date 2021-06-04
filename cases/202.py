# 输出乘法口诀表 
'''
输入1个整数n，输出n * n的乘法口诀表。用制表符分隔。

如果输入的n大于20，则取n = 20。
'''

n = int(input())

if n > 20:
    n = 20

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
