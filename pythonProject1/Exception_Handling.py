try:
    num =[10, 0, 20]
    dev = num[0] / num[0]
    print(dev)
except SyntaxError:
    print('My Wrong')
except ZeroDivisionError:
    print('Dividing zero is not Possible')
except IndexError:
    print('list index out of range')
except TypeError:
    print('Dividing String is not Possible')
finally:
    print('Complete')
