# 用for循环实现偶数求和 
'''
输入1个整数n，输出2 + 4 + ... + （n或n前的最后一个偶数）的值。
'''

n = int(input())
print(sum(range(2, n, 2)))
