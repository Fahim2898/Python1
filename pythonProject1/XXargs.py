'''
def information(id, name, age, cgpa):
    print('Id=', id)
    print('Name=', name)
    print('Age=', age)
    print('CGPA=', cgpa)
    print()


information(2898, 'Md. Fahim Bhuiyan', 19.8, 3.80)
information(2901, 'Md. Mukim', 24, 3.25)
information(2838, 'Annoy', 19.9, 3.73)
information(2898, 'Md. Alve Bhuiyan', 16, 0)
'''

'''
def inputinfo(id, name, age, cgpa):
    id = int(input('Enter Your Id:'))
    name = input('Enter Your Name:')
    age = input('Enter Your Age:')
    cgpa = input('Enter Your CGPA:')
    print ()                

def information(id, name, age, cgpa):
    print('Id=', id)
    print('Name=', name)
    print('Age=', age)
    print('CGPA=', cgpa)
    print()


inputinfo (id, "name", "age", "cgpa")
information(id, "name", "age", "cgpa")
'''
#xxargs


def student(**info):
    print(info)


student(name='Fahim', id=2898)


