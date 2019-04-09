# x, y, z = 5, 7, 10
# print(x, y, z)
#
# if x % 2 != 0:
# 	pass
# else:
# 	x = 0
#
# if y % 2 !=0:
# 	pass
# else:
# 	y = 0
#
# if z % 2 !=0:
# 	pass
# else:
# 	z = 0
#
# if x > y and x > z and x % 2 != 0:
# 	print("The largest odd number is x, and x = ", x)
# elif y > x and y> z and y % 2 != 0:
# 	print("The largest odd number is y, and y  = ", y)
# elif z % 2 != 0:
# 	print("The largest odd number is z, and z = ", z)
# else:
# 	print("None of the numbers are odd" )
#
#
#
# numXs = int(input('how many times should I print the letter X '))
# toPrint = ''
# while abs(numXs) != 0:
#     toPrint = toPrint + 'x'
#     numXs = abs(numXs)-1
# print(toPrint)


# This program asks the user to input 10 integers and then prints the largest odd number entered.
# i = 10
# x = 0
# number = 0
# while i != 0:
# 	number = int(input('please enter a digit '))
# 	if number > x and number % 2 != 0:
# 		x = number
#
# 	i = i-1
#
# print(x)



## Find the cube root of a perfect cube
# x = int(input('Enter an integer: '))
# ans = 0
# while ans**3 < abs(x):
# 	ans = ans +1
# if ans**3 != abs(x):
# 	print(x, 'is not a perfect cube')
# else:
# 	if x < 0:
# 		ans = -ans
# 	print('Cube root of', x, 'is', ans)


## Finger exercise: Write a program that asks the user to enter an integer and prints two integers, root
## and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no
## such pair of integers exists, it should print a message to that effect.
# i = 0
# x = int(input('Enter an integer: '))
# p = 1
# ans = 0
# prints = 0
#
# while p < 6:
# 	while ans ** p < abs(x):
# 		ans = ans + 1
# 	if ans ** p != abs(x):
# 		pass
# 	else:
# 		if x < 0:
# 			ans = -ans
# 		if x < 0 and p % 2 == 0:
# 			pass
# 		else:
# 			print(ans, '^', p, '=', x)
# 			prints = prints + 1
#
# 	ans = 0
# 	p = p + 1
# if prints == 1:
# 	print('There are no more roots and powers for this integer.')


# x = 4
# for j in range(x):
# 	for i in range(x):
# 		print(i)
# 		x = 2

# total = 0
# a = 1
# while a != 0:
# 		a = float(input('Enter the number to sum. To stop the sum and produce the result enter 0: '))
# 		total = total + a
#
# print(total-1)


###############
## Finger exercise: Let s be a string that contains a sequence of decimal numbers separated by commas,
## e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s.

s = 1.2, 1.3, 1.2, 1.5, 1.6, 1.4
x = 0

for i in s:
	x = x + i

print(x)


'''Write a program that asks the user to input 10 integers, and
then prints the largest odd number that was entered. If no odd number was
entered, it should print a message to that effect.'''

max = None

i = 0
while i < 10:
  n = int(input())
  if (max and n % 2 != 0 and n > max) or (not max and n % 2 != 0):
    max = n
  i += 1

if max:
  print(max)
else:
  print("All even.")

'''© 2019 GitHub, Inc.'''
