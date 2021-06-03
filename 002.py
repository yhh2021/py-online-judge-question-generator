# 比较运算符和逻辑运算符的使用
'''
输入8个整数a1 .. a8，分别输出以下逻辑表达式的值：
a1 == a2
a3 > a4
a5 < a6
not (a7 != a8)
'''

a1, a2, a3, a4, a5, a6, a7, a8 = map(int, input().split())
print(a1 == a2, a3 > a4, a5 < a6, not (a7 != a8))