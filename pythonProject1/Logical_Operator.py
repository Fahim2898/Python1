num1 = 200
num2 = 100
num3 = 90

# And Operator
if num1 > num2 and num1 > num3:
    print('Maximum=', num1)
elif num2 > num1 and num2 > num3:
    print('Maximum=', num2)
else:
    print('Maximum=', num3)

# Or Operator

app = (input("Enter your Alphabet:"))
app = app.lower()
if app == 'a' or 'e' or 'i' or 'o' or 'u':
    print("Your Alphabet is Vowel")
else:
    print("Your Alphabet is consonant")
