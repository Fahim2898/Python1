numberOfLater = 0
numberOfNumber = 0
numberOfWord = 1

text = input('Enter Your Text:')

for i in text:
    i = i.lower()
    if 'a' <= i <= 'z':
        numberOfLater = numberOfLater + 1
    elif '0' <= i <= '9':
        numberOfNumber = numberOfNumber + 1
    elif i ==' ':
        numberOfWord = numberOfWord + 1
print('Number Of Later =', numberOfLater)
print('Number Of Number =', numberOfNumber)
print('Number Of Word =', numberOfWord)