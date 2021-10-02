subject = ['C', 'C++', 'C#', 'Java', 'JavaScript', 'Python', 'PHP']

print(subject)

print(subject[0])    #0 number index r value print or 1 st value print
print(subject[5])    #5 number index r value print or 6th value print
print(subject[2:5])     #2 to (5-1) number index r value print
print(subject[-1])      #last value print

print('Python' in subject)      #python list a asa ki nah ta check

print('R' in subject)           #R list a asa ki nah ta check

print(subject + ['R'])          # list a 'R' Add temporally

print('Length=', len(subject))      # length check

subject.insert(2, 'R')
print('Insert \'R\' in 2nd index=', subject)

subject.remove('C#')
print('Remove C#=', subject)

subject.sort()
print('Sort=', subject)

index_python = subject.index('Python')
print('Python Index=', index_python)

Number =[5, 10, 15, 20, 25, 30, 2, 4, 8, 10]
Number.sort()
print('Sort=', Number)

Number.pop()
print('Pop=', Number)

Number.reverse()
print('Reverse=', Number)

number = Number.copy()
print('Copy from Number =', number)

Number.insert(4, 11)
print('Insert 11 in index 4=', Number)

x = [2, 30, 99, 32, 73, 81, 93]
x.sort()
print('Sort=', x)