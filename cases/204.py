# GCD & LCD 
'''
输入2个整数，输出它们的最大公约数和最小公倍数。
'''
x, y = map(int, input().split())

if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(factor)
        print((x * y // factor))
        break
