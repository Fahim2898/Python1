class Student:
    sid = ''
    name = ''
    gpa = ''

    def __init__(self, sid, name, gpa):   #Constructor --> Spical type of Mathod
        self.sid = sid
        self.name = name
        self.gpa = gpa

    def print_value(self):  # mathod
        print(f'ID: {self.sid}\nName: {self.name}\nGPA: {self.gpa}')
        print()


fahim = Student(102, 'Md. Fahim Bhuiyan', 3.81)
'''
fahim.sid = 102
fahim.name = 'Md. Fahim Bhuiyan'
fahim.gpa = 3.81
'''
fahim.print_value()

farhan = Student(105, 'Farhan', 3.98)
farhan.print_value()

