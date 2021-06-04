# 闰年判断 
'''
输入1个整数年份，输出判断结果。
'''

year = int(input())
is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
print(is_leap)
