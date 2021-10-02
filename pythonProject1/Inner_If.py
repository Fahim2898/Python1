num1 = float(input("Enter your 1st Number:"))
num2 = float(input("Enter your 2nd Number:"))
num3 = float(input("Enter your 3rd Number:"))

if num1 > num2:
    if num1 > num3:
        print('Maximum Number= ', num1)
    else:
        print('Maximum Number= ', num3)

elif num1 < num2:
    if num2 > num3:
        print('Maximum Number= ', num2)
    else:
        print('Maximum Number= ', num3)
