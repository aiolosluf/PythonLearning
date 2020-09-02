"""
in/cm exchange
"""
# value = float(input('please enter value:'))
# unit = input('please enter unit:')
# if unit == 'in':
#     print('%fin equals %fcm' % (value, value*2.54))
# elif unit =='cm':
#     print('%fcm equals %fin' % (value, value/2.54))
# else:
#     print('incorrect unit.')
    
    
"""
score rate calculate
"""
# score = int(input('please enter score:'))
# if score>=90:
#     print('grade A')
# elif score>=80:
#     print('grade B')
# elif score>=70:
#     print('grade C')
# elif score>=60:
#     print('grade D')
# else:
#     print('grade E')

"""
triangle area
"""
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a+b>c and a+c>b and b+c>a:
    print('parameter=',a+b+c)
    p = (a+b+c)/2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('area=',area)
else:
    print('can\'t form a triangle')
    
    