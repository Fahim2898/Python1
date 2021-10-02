name = input("Enter Your Name: ")
id = input ("Enter Your ID:")
number = float(input("Enter Your Mark:"))
print("Name: " +name)
print("ID: ",id,)

if 80 <= number <= 100:
    print('A+')
elif 75 <= number <= 79:
    print('A')
elif 70 <= number <= 74:
    print('A-')
elif 65 <= number <= 69:
    print('B+')
elif 60 <= number <= 64:
    print('B')
elif 55 <= number <= 59:
    print('B-')
elif 50 <= number <= 54:
    print('C+')
elif 45 <= number <= 49:
    print('c')
elif 40 <= number <= 44:
    print('B')
elif 0 <= number <= 39:
    print('Fail')
else:
    print('invalid Input')
