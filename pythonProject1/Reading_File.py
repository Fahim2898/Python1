file = open('Fahim.txt', 'r+')

print(file.writable())
print(file.readable())
print(file.read())
file.close()