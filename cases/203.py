# 质数判定 
'''
输入1个整数n，判断它是不是质数。
'''
from math import sqrt

num = int(input())

end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
print(is_prime and num != 1)

