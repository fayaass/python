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


'''a=int(input("enter a number:"))
d=a%10
if d%3==0:
    print("number is divisible by 3")
else:
    print("not divisible")'''


    #if-else-if ladder

'''if cond:
    stm
elif cond:
    stm
else:
    stm'''

'''a=10
b=11
if a==b:
    print('equal')
elif a>b:
    print(a)
else:
    print(b)'''

    #nextelif

'''if cond:
        if cond:
            stm
        else:
            stm
else:
    stm'''


'''name=(input("enter name :"))
age=int(input("enter age:"))
weight=float(input("enter weight:"))

print("name :",name)
print("age :",age)
print("weight :",weight)'''


'''a=int(input("enter a number: "))
if a==1:
    print("sunday")
elif a==2:
    print("monday")
elif a==3:
    print("tuesday")
elif a==4:
    print("wednesday")
elif a==5:
    print("thursday")
elif a==6:
    print("friday")
elif a==7:
    print("saturday")
else:
    print("invalid section")'''



'''a=(input("enter the city name :"))
if a=="Delhi":
    print("Red Fort")
elif a=="Agra":
    print("Tal Mahal")
elif a=="Jaipur":
    print("Jal Mahal")
else:
    print("invalid")'''


'''a=int(input("enter the cost of the bike:"))
if a>100000:
    print(a*0.15)
elif a>50000 and a<=100000:
    print(a*0.10)
else:
    print(a*0.05)'''



'''a=int(input("enter the unit:"))
if a<=100:
    print("no charges")
elif a>100 and a<=200:
    print((a-100)*5)
elif a>=200:
    print((a-200)*10+500)
else:
    print("invalid")'''

#while condition:
    #statement
    #incremet/decrement


                            #while loop



'''i=1
while i<=10:
    print(i)                            #print 1-10
    i+=1'''


'''a=int(input("enter the first number :"))
b=int(input("enter the second number :"))

while a<=b:
    print(a)                            #print a-b
    a+=1'''



'''a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
c=0
while a<=b:
    c+=a                                #sum of a-b
    a+=1
print(c)'''


'''a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
while a<=b:
    if a%2!=0:                          #odd numbers
        print(a)
    a+=1'''




'''a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
c=0
while a<=b:                             
    if a%2!=0:                          #sum of odd numbers
        c+=a
    a+=1
print(c)'''



'''i=1
a=int(input("enter a number :"))
while i<=10:                            #multiplication
    print(i,"*",a,"=",a*i)
    i+=1'''



'''i=1
a=int(input("enter a number :"))
s=1
while i<=a:
      s*=i                              #factorial
      i+=1
print(s)
'''


'''a=int(input("enter a number :"))
rev=0
while a>0:
    d=a%10
    rev=rev*10+d                        #reverse of a number
    a//=10
print(rev)'''




'''a=(input("enter a string :"))
rev=""
i=0
l=len(a)
while i<l:                              #reverse of a string
    #print(a[i])
    rev=a[i]+rev
    i+=1
print(rev)'''




                            #for loop

    
#range(limit)
'''for i in range(10):
    print(i)'''


#range(start,end)
'''for i in range(2,11):
    print(i)'''



#range(start,end,updation)
'''for i in range(2,11,2):
    print(i)'''


'''a="python"
for i in a:
    print(i)'''



'''a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
s=0
for i in range(a,b+1):                          #sum of a-b in forloop
    s+=i
print(s)'''


'''a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
for i in range(a,b+1):
    if i%2!=0:                                  #odd numbers using forloop
        print(i)'''


'''a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
s=0
for i in range(a,b+1):                          
    if i%2!=0:                                  #sum of odd numbers using for loop
        s+=i
print(s)'''




'''a=int(input("enter a number:"))
for i in range(1,11):                           #multiplication using for loop
    print(i,"*",a,"=",a*i)'''



'''a=int(input("enter a number:"))
s=1
for i in range(1,a+1):                          #factorial using for loop
      s*=i
print(s)'''



'''a=(input("enter a string:"))
rev=""
for i in a:                                    #reverse of a string using for loop  
    rev=i+rev
print(rev)
'''

                #loop statements


#break

'''for i in range(10):
    print(i)
    if i==5:
        break
'''

#continue

'''for i in range(10):
    if i==5:
        print("it's value 5")
        continue
    print(i)'''


#pass

'''for i in range(10):
    pass
'''


'''a=int(input("enter a number:"))
rev=0
for i in range(a):
    d=a%10
    rev=rev*10+d
    a//=10
    if a==0:
        break
print(rev)'''



'''a=(input("enter a word :"))
for i in (a):
    if i%2==0:  
     print(i)

'''


'''a=(input("enter a word :"))'''





                #LIST

'''l=[1,2,10,20,'abc',1]'''
'''print(l[0])
print(l[1])'''


'''if 10 in l:
    print('available')
else:
    print('not available')'''


# for i in l:
#     print(i)


# l[0]=11
# print(l)


#                 #list methods

# #1.append()
# #2.extend
# #3.insert

#     #append

# l=[]

# l.append(10)
# print(l)

# l.append('abc')
# print(l)

# l.append([10,11,12])
# print(l)

# if 12 in l:
#     print('available')
# else:
#     print('not available')

#     #extend

# l.extend([100,200,300])
# print(l)

#        #insert

# l.insert(2,'hello')
# print(l)


            #delete methods

#1.clear
#2.pop 1.pop() 2.pop(index)
#3.remove

# l=[10,20,30]

    #clear

# l.clear()
# print(l)

    #pop

# l.pop()
# print(l)

# l.pop(1)
# print(l)


    #remove

# l.remove(10)
# print(l)


# l=[10,10,20,30,8,5]

# print(l.index(20))
# print(l)

# print(l.count(30))
# print(l)

# l.sort()
# # print(l)

# l.reverse()
# print(l)


            #sum of the list{int,float}

# l=[1,10,12,'abc',8.5]
# s=0
# for i in l:
#     if type(i)==int or type(i)==float:
#         s+=i
# print(s)

            #sum of odd and even numbers in the list

# l=[10,1,2,3,5,8,6]
# even=0
# odd=0
# for i in l:
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(even)
# print(odd)


            #remove the same numbers in the list
#1.

# l=[10,1,2,3,5,8,6,1,3,8]
# s=set(l)
# l=list(s)
# print(l)

#2. in/not in

# l=[10,1,2,3,5,8,6,1,3,8]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

#3.

# l=[10,1,2,3,5,8,6,1,3,8] 
# for i in l:
#     if l.count(i)>=2:
#         l.remove(i)
# print(l)



l=[10,1,2,3,5,8,6,1,3,8]










