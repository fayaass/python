from add import *
from numbers import *
from sub import *
from mul import *
from div import *
from mod import *

while True:
    print('''
    1.add
    2.sub
    3.mul
    4.div
    5.mod
    6.exit
    ''')
    choice=int(input('enter your choice :'))
    if choice==1:
        a,b=num()
        add(a,b)
    elif choice==2:
        a,b=num()
        sub(a,b)
    elif choice==3:
        a,b=num()
        mul(a,b)
    elif choice==4:
        a,b=num()
        div(a,b)
    elif choice==5:
        a,b=num()
        mod(a,b)
    elif choice==6:
        break
    else:
        print('invalid choice')