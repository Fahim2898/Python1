text = input("Enter your Sentence:")

print('Length=', len(text)),
alp = 0
num = 0
word = 1
for i in text:
    if 'a' <= i <= 'z':
        i = i.lower()
        alp = alp + 1
    elif '0' <= i <= '9':
        num = num + 1
    elif i == ' ':
        word = word + 1

print(f'Alphabet= {alp}\nNumber= {num}\nWord= {word}')
