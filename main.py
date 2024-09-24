from add import *
from numbers import *
while True:
    print('''
    1.add
    2.sub
    3.mul
    ''')
    choice=int(input('enter your choice :'))
    if choice==1:
        a,b=num()
        add(a,b)