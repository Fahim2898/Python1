#1+2+3+4+5+_______+n

number =int(input('Enter Your Last Number:'))
sum =0
for x in range(1, number+1, 1):
    sum =sum + x
print('1+2+3+4+____+n =', sum)

#2+4+6+8+____+n
sum=0
for x in range(2, number+1, 2):
    sum =sum + x
print('2+4+6+8+____+n =', sum)

#1+3+5+7+_____+n
sum=0
for x in range(1, number+1, 2):
    sum =sum + x
print('1+3+5+7+____+n =',sum)

#4+8+12+____+n
sum=0
for x in range(4, number+1, 4):
    sum =sum + x
print('4+8+12+____+n =',sum)

#1^2 +2^2 +3^2 +____+n^2
sum =0
for x in range(1, number+1, 1):
    sum =sum + pow(x, 2)
print('1^2 +2^2 +3^2 +____+n^2 =', sum)

#2^2 +4^2 +6^2 +____+n^2
sum=0
for x in range(2, number+1, 2):
    sum = sum + pow(x, 2)
print('2^2 +4^2 +6^2 +____+n^2 =', sum)

#Factorial
sum = 1
for x in range(1, number+1, 1):
    sum = sum*x
print('Factorial of', number, '!=', sum)

