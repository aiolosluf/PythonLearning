"""
guess number
# """

# import random

# num = random.randint(1,100)
# count = 0


# while True:
#     guess = int(input('enter number:'))
#     count+=1
#     if guess>num:
#         print('a little smaller')
#     elif guess<num:
#         print('a little bigger')
#     else:
#         print('bingo!')
#         break
    

# print('total guess: %d' % count)

    
"""
prime number
"""

from math import sqrt

num = int(input('enter a number:'))
end = int(sqrt(num))
is_prime = True
for x in range(2,end+1):
    if num%x == 0:
        is_prime = False
        break
if is_prime and num!=1:
    print('%d is prime' % num)
else:
    print('%d is not prime' % num)