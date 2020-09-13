# a = 10
# b = 3
# a += b        # 相当于：a = a + b
# a *= a + 2    # 相当于：a = a * (a + 2)
# print(a)      # 算一下这里会输出什么

# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# radius = float(input('input radius:'))
# parameter = 2*3.1415926*radius
# area = radius*radius*3.1415926
# print('%.1f radius gets parameter: %.1f, gets area: %.1f' %(radius, parameter,area))

year = int(input('which year:'))
is_leap = year%4 == 0 and year%100 != 0 or \
    year%400 == 0
print(is_leap)

