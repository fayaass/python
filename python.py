#datatypes

'''print("Welcome")
#print('Welcome')
#print("Welcome")
print("Welcome")
print("Welcome")

a="Welcome123"
print(a)

std_roll = 20
print(std_roll)

#2a = 20
a2 = 20

_a=10
print(_a)


a=123
print(a)
print(type(a))

b=str(a)
print(a)
print(type(b))

c=int(b)
print(b)
print(type(c))

d=float(c)
print(c)
print(type(d))

#OPERATORS

    #arithmeticoperators

# +,-,*,/,%,//,**

print(10+5)
print(10-5)
print('muhammed'+'fayas')

a=10
b=5
print(a*b)

print(10/3)
print(10//3)

print(10%3)

print(10*10*10)
print(10**3)

    #assignmentoperators

# =,+=,-=,*=,/=,%=,//=,**=

a=10
print(a)

a=10
#a=a+5
a+=5
print(a)

a=10
#a=a-5
a-=5
print(a)

a=10
#a=a*5
a*=5
print(a)

a=10
#a=a/2
a/=5
print(a)

a=10
#a=a%3
a%=3
print(a)

a=10
#a=a//5
a//=5
print(a)

a=10
#a=a**5
a**=5
print(a)

    #comparisonoperators

# ==,!=,>,<,>=,<=

print(10==10)
print(10==11)

print(10!=10)
print(10!=11)

print(10>9)
print(10>11)

print(10<9)
print(10<11)

print(10>=9)
print(10>=10)
print(10>=11)

print(10<=11)
print(10<=10)
print(10<=9)

    #logicaloperators

# and,or,not

    #and

print(True and True) #true
print(True and False) #false
print(False and True) #false
print(False and False) #false

print(10==10 and 11==11)
print(10==1 and 10==11)

    #or

print(True and True) #true
print(True and False) #true
print(False and True) #true
print(False and False) #true

print(10==11 or 10==10)

    #not

print(not(False)) #true
print(not(True)) #false

print(not(10==11))
print(not(10==10))


    #membershipoperators

#in,not in

    #in

print('p' in 'python') #true
print('f' in 'python') #false

    #not in

print('p' not in 'python') #false
print('f' not in 'python') #true

l=[10,11,12,13]
print(10 in l)

    #identityoperator

#is,is not

# a=10
# b=10
# print(a==b)

    #is

a=10
b=10
print(id(a))
print(id(b))
print(a is b) #true

    #is not

a={1,2,3}
b={1,2,3,4}
print(id(a))
print(id(b))
print(a is not b)



    #addinput

name=(input("enter name :"))
age=int(input("enter age:"))
weight=float(input("enter weight:"))

print("name :",name)
print("age :",age)
print("weight :",weight)'''


    #if-else statement

#if condition:
   #statement
#else:
   #statement 


'''if 10==10:
    print('equal')
else:
    print('not equal')

if 10==11:
    print('equal')
else:
    print('not equal')



a=(input("enter a number:"))
b=(input("enter another number:"))
if a==b:
    print('equal')
else:
    print('not equal')


a=(input("enter a number:"))
b=(input("enter another number:"))
if a>b:
    print('a is largest')
else:
    print('b is largest')'''



'''a=int(input("enter the salary:"))
b=int(input("year of experience:"))
if b>=5:
    print(a*0.05)
else:
    print("no bonus available")


a=int(input("enter the salary:"))
b=int(input("year of experience:"))
if b>=5:
    print(a*0.05)
else:
    print(a*0.03)'''


a=int(input("enter a number:"))
d=a%10
if d%3==0:
    print("number is divisible by 3")
else:
    print("not divisible")







