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



#checking palindrome

# l=['malayalam','apple','amma','python']
# for i in l:
#     rev=i[::-1]
#     if rev==i:
#         print(rev,'its palindrome')
#     else:
#         print(rev,'its not palindrome')


# list of numbers divisible by 3

# l=[1,2,5,8,9,3,12]
# for i in l:
#     if i%3==0:
#         print(i,'divisible')
#     else:
#         print(i,'not divisible')



# <----------choice------------>

# while True:
#     print('''
# 1.add
# 2.sub
# 3.mul
# 4.div
# 5.exit
#           ''')
    
#     choice=int(input("enter your choice :"))
#     if choice==1:
#         a=int(input("enter first no :"))
#         b=int(input("enter second no :"))
#         c=a+b
#         print(c)
#     elif choice==2:
#         a=int(input("enter first no :"))
#         b=int(input("enter second no :"))
#         c=a-b
#         print(c)
#     elif choice==3:
#         a=int(input("enter first no :"))
#         b=int(input("enter second no :"))
#         c=a*b
#         print(c)
#     elif choice==4:
#         a=int(input("enter first no :"))
#         b=int(input("enter second no"))
#         c=a/b
#         print(c)
#     elif choice==5:
#         break
#     else:
#         print("invalid choice")


#----------------------------------------------------------------------------------

#student details using list

# std=[['a',20,50],['b',20,50],['c',20,50],['d',20,50]]
# while True:
#  print('''
# 1.student details
# 2.view std details
# 3.upadte std details
# 4.delete std details
# 5.exit
#           ''')
 
#  choice=int(input("enter your choice :"))
#  if choice==1:
#          name=str(input("enter name :"))
#          age=int(input("enter age :"))
#          mark=int(input("enter mark :"))
#          std.append([name,age,mark])
#  elif choice==2:
#       for i in std:
#            print(i)
#  elif choice==3:
#       name=str(input("enter name :"))
#       f=0
#       for i in std:
#            if name in i:
#              mark=int(input("enter mark :"))
#              i[2]=mark
#              f=1
#       if f==0:
#                print('invalid name')
#  elif choice==4:
#       name=str(input("enter name :"))
#       f=0
#       for i in std:
#            if name in i:
#              std.remove(i)
#              f=1
#       if f==0:
#                print('invalid name')
#  elif choice==5:
#      break
#  else:
#      print('invalid choice')


#------------------------------------------------------------------------------------

#employee details using list

# emp=[['fayas',203,24,'Delhi',75000,'manager',4],['yaseen',204,24,'Delhi',20000,'security',10]]
# import datetime
# while True:
#  print('''
# 1.register
# 2.view
# 3.update
# 4.delete
# 5.add work
# 6.search
# 7.exit
#  ''')
#  choice=int(input('enter the choice :'))
#  if choice==1:
#     name=str(input('enter name :'))
#     id=int(input('enter id :'))
#     age=int(input('enter age :'))
#     place=str(input('enter place :'))
#     salary=int(input('enter salary :'))
#     position=str(input('enter position :'))
#     experience=int(input('enter experience :'))
#     emp.append([name,id,age,place,salary,position,experience])


#  elif choice==2:
#     for i in emp:
#         print(i)


#  elif choice==3:
#     name=str(input('enter name :'))
#     f=0
#     for i in emp:
#         if name in i:                                                                            
#             choice=int(input('enter the choice :'))
#             if choice==1:
#                 age=int(input('enter age :'))
#                 i[2]=age                                                                      
#             elif choice==2:
#                 place=str(input('enter place :'))
#                 i[3]=place
#             elif choice==3:
#                 salary=int(input('enter salary :'))
#                 i[4]=salary
#             elif choice==4:
#                 position=str(input('enter position :'))
#                 i[5]=position
#             elif choice==5:
#                 experience=int(input('enter experience :'))
#                 i[6]=experience
#             f=1
#         if f==0:
#                 print('invalid name')


#  elif choice==4:
#     name=str(input('enter name :'))
#     f=0
#     for i in emp:
#         if name in i :
#             emp.remove(i)
#             f=1
#     if f==0:
#             print('invalid name')


#  elif choice==5:
#      id=int(input('enter an id :'))
#      for i in emp:
#          if id in i:
#              task=input('enter the task :')
#              date=datetime.datetime.now().strftime('%x')
#              i.append([task,date])
#              print(emp)
     

#  elif choice==6:
#     name=str(input('enter name :'))
#     f=0
#     for i in emp:
#         if name in i :
#             print(i)
#             f=1
#     if f==0:
#             print('invalid name')


#  elif choice==6:
#      break
 

#  else:
#      print('invalid choice')



                    #tuple

# t=(1,2,3)
# print(t)

# t1=(1,)
# print(t)

# t2=('abc',)
# print(t2)

# t=10,11,12
# print(t)

#list in tuple

# t=(10,[1,2,3],12)
# # print(t[1])
# t[1].append(4)
# print(t)

#how to change values in tuple 

# t=(1,2,3)
# l=list(t)
# print(l)
# l.pop()
# print(l)
# t=tuple(l)
# print(t)


#find the position of the values using tuple

# t=(1,2,3,4,1,2,3,5,3,6)
# a=int(input("enter a value :"))
# c=t.count(a)
# print(c)
# pos=0
# while c>0:
#     p=t.index(a,pos)
#     pos=p+1
#     print('index:',p)
#     c-=1



#dictionary


# d={'name':'fayas','age':22,'place':'kottayam'}
# print(d)
# print(d['name'])
# print(d['age'])
# print(d['place'])

# for i in d:
#     print(i,d[i])

# d['age']=23
# print(d)

# d['mark']=50
# print(d)


# for i in d:
#     print(i,d[i])


# if d['age']==22:
#     print('available')
# else:
#     print('not available')

# print(d.get('name'))

# print(d.items())

# print(d.values())


# for i in d.values():
#     print(i)


# print(d.keys())

# a=d
# a=d.copy()
# print(id(a))
# print(id(d))
# d['mark']=45
# print(a)
# print(d)

# d.pop('place')
# print(d)

# d.popitem()
# print(d)

# d.setdefault('mark')
# print(d)

# l=[10,11,12]
# print(d.fromkeys(l))



# name=str(input("enter name :"))
# age=int(input("enter age:"))
# place=str(input("enter place :"))
# mark=int(input("enter mark :"))


# d['name']=name
# d['age']=age
# d['place']=place
# d['mark']=mark

# print(d)


                    #shop details using dictionary

# shop=[{'name':'book','id':'1','price':'50','stock':'8'},{'name':'pen','id':'2','price':'10','stock':'20'}]
# while True:
#     print('''
# 1.product details
# 2.view shop details
# 3.update shop details
# 4.delete shop details
# 5.exit              
#           ''')
#     choice=int(input('enter the choice :'))


#     if choice==1:
#         name=str(input('enter name :'))
#         id=int(input('enter id :'))
#         price=int(input('enter price :'))
#         stock=int(input('enter stock :'))
#         shop.append({'name':name,'id':id,'price':price,'stock':stock})


#     elif choice==2:
#         for i in shop:
#             print(i)


#     elif choice==3:
#         name=str(input('enter name :'))
#         f=0
#         for i in shop:
#             if name == i['name']:
#                 print('''
#                 1.price update
#                 2.stock update
#                       ''')
#                 choice=int(input('enter the choice :'))
#                 if choice==1:
#                     price=int(input('enter price :'))
#                     i['price']=price
#                 elif choice==2:
#                     stock=int(input('enter stock :'))
#                     i['stock']=stock
#             f=1
#             if f==0:
#                 print('invalid choice')


#     elif choice==4:
#         name=str(input('enter name :'))
#         f=0
#         for i in shop:
#             if name == i['name']:
#                 shop.remove(i)
#                 f=1
#             if f==0:
#                 print('invalid choice')


#     elif choice==5:
#         break
#     else:
#         ('invalid option')


            #library management using dictionary
            

# library=[{'bookname':'Lord of the Flies','id':'1','price':'199','stock':'6'},{'bookname':'To Kill a Mockingbird','id':'2','price':'240','stock':'10'},
#          {'bookname':'The Alchemist','id':'3','price':'399','stock':'14'}]
# while True:
#     print('''
# 1.product details
# 2.view shop details
# 3.update shop details
# 4.delete shop details
# 5.exit              
#           ''')
#     choice=int(input('enter the choice :'))
#     if choice==1:
#         bookname=str(input('enter name :'))
#         id=int(input('enter id :'))
#         price=int(input('enter price :'))
#         stock=int(input('enter stock :'))
#         library.append({'bookname':bookname,'id':id,'price':price,'stock':stock})
#     elif choice==2:
#         for i in library:
#             print(i)
#     elif choice==3:
#         bookname=str(input('enter name :'))
#         f=0
#         for i in library:
#             if bookname == i['bookname']:
#                 print('''
#                 1.price update
#                 2.stock update
#                       ''')
#                 choice=int(input('enter the choice :'))
#                 if choice==1:
#                     price=int(input('enter price :'))
#                     i['price']=price
#                 elif choice==2:
#                     stock=int(input('enter stock :'))
#                     i['stock']=stock
#             f=1
#             if f==0:
#                 print('invalid choice')
#     elif choice==4:
#         bookname=str(input('enter name :'))
#         f=0
#         for i in library:
#             if bookname == i['bookname']:
#                 library.remove(i)
#             f=1
#         if f==0:
#                 print('invalid choice')
#     elif choice==5:
#         bookname=str(input('enter name :'))
#         f=0
#         for i in library:
#             if bookname == i['bookname']:
#                 print(i)
#             f=1
#         if f==0:
#                 print('invalid choice')
#     elif choice==5:
#         break
#     else:
#         ('invalid option')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


#task1

# fwr=[['shoe',1,8,'adidas',2999,6],['slider',2,7,'nike',1299,8],['boots',3,9,'woodland',5999,7]]
# while True:
#  print('''
# 1.product details
# 2.view product details
# 3.upadte product details
# 4.search product details
# 5.delete product details
# 6.exit
#           ''')
 
#  choice=int(input("enter your choice :"))
#  if choice==1:
#          product=str(input("enter product :"))
#          id=int(input("enter id :"))
#          size=int(input("enter size :"))
#          brand=str(input("enter brand :"))
#          price=str(input("enter price :"))
#          stock=int(input("enter stock :"))
#          fwr.append([product,id,size,price,brand,stock])
#  elif choice==2:
#       for i in fwr:
#            print(i)
#  elif choice==3:
#     id=int(input("enter id :"))
#     f=0
#     for i in fwr:
#         if id in i:                                                                            
#             while True:
#                  print('''
#                     1.product
#                     2.size''')
#                  choice=int(input('enter the choice :'))
#                  if choice == 1:
#                         product=str(input('enter product :'))
#                         i[0]=product
#                     elif choice==2:
#                         size=int(input('enter size :'))
#                         i[2]=size                                                                      
#                     elif choice==3:
#                         brand=str(input('enter brand :'))
#                         i[3]=brand
#                     elif choice==4:
#                         price=int(input('enter price :'))
#                         i[4]=price
#                     elif choice==5:
#                         stock=str(input('enter stock :'))
#                         i[5]=stock
#                     f=1
#     if f==0:
#                 print('invalid name')
#  elif choice==4:
#       id=int(input("enter id :"))
#       f=0
#       for i in fwr:
#            if id in i:
#              print(i)
#              f=1
#       if f==0:
#                print('invalid name')
#  elif choice==5:
#       id=int(input("enter id :"))
#       f=0
#       for i in fwr:
#            if id in i:
#              fwr.remove(i)
#              f=1
#       if f==0:
#                print('invalid name')
#  elif choice==6:
#      break
#  else:
#      print('invalid choice')

#-----#------------------------------------------------------------------------------------------------------------------------------------------------------------------


# data=[{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':45}]

# # for i in data:
# #     print(i['age'])

# print('{:<10}{:<10}'.format('name','age'))
# print('-'*20)
# for i in data:
#     if i['age']<=30:
#         print('{:<10}{:<10}'.format(i['name'],i['age']))

# print('{:<10}{:<10}'.format('name','age'))
# print('-'*20)
# for i in data:
#     if i['age']>30:
#         print('{:<10}{:<10}'.format(i['name'],i['age']))


# data=[{'name':'a','age':22},{'name':'c','age':20},{'name':'b','age':30},{'name':'c','age':45}]
# a=[]
# b=[]
# for i in data:
#     if i['age']<=30:
#         a.append(i)
#     else:
#         b.append(i)
# print(a)
# print(b)


# data=[{'name':'a','age':22},{'name':'c','age':20},{'name':'b','age':30},{'name':'c','age':45}]
# a=[i for i in data if i ['age']<=30]
# b=[i for i in data if i ['age']>30]
# print(a)
# print(b)


# l=[1,2,3,4,5,6,7,8,9,10]
# even=[i for i in l if i%2==0]
# odd=[i for i in l if i%2!=0]
# print(even)
# print(odd)

#---------------------------------------------------------------------------------------------------------------------------------------------

# dict={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# num=int(input('enter a number :'))
# s=''
# while num>0:
#     d=num%10
#     s=dict[d]+'  '+s
#     num//=10
# print(s)


# l=[{'name':'fayas','age':22,'project':['ems','sms']}]
# print(l[0]['project'][0])


# d={'name':'fayas','age':22}
# print(d['age'])


# l=[{'name':'fayas','age':22,'project':['ems','sms']}]
# a=str(input('enter a word :'))
# for i in l:
#     i['project'].append(a)
#     print(i)

#set

# s={1,4,5,7,'abc',5.8,1}

# for i in s:
#     print(i)

# if 7 in s:
#     print('true')
# else:
#     print('false')

# print(s)


# l=[1,2,3,5,1,2,3,4]
# s=set(l)
# print(s)
# l=list(s)
# print(l)


# s=set()         #to create an empty set.
# s.add(13)
# print(s)

# s={10,11,12}
# s.pop()
# print(s)

# s.discard(100)
# print(s)

# s.remove(10)
# print(s)

# s.clear()
# print(s)


# s={1,2,3,4,5}
# s1={1,2,3,6}
# s2={6,7,8}

# print(s.difference(s1))

# print(s.union(s1))

# print(s.intersection(s1))

# print(s.symmetric_difference(s1))

# print(s.isdisjoint(s2))

# print(s.issubset(s1))

# print(s.issuperset(s1))

# s.update({7,8,9})
# print(s)

# s.difference_update(s1)
# print(s)

# s=set()
# b=int(input('enter the limit :'))
# for i in range (b):
#     name=str(input('enter the name :'))
#     s.add(name)
#     print(s)



# php=set()
# java=set()
# python=set()
# b=int(input('enter the limit :'))
# for i in range (b):
#     name=str(input('enter the name :'))
#     php.add(name)
#     print(php)
#     java.add(name)
#     print(java)
#     python.add(name)
#     print(python)

# php=set()
# java=set()
# python=set()
          
# php={'a','b','c'}
# a=int(input('enter the limit :'))
# for i in range (a):
#     name=str(input('enter the name :'))
#     php.add(name)
#     print(php) 

# java={'a','c','d','e'}
# b=int(input('enter the limit :'))
# for i in range (b):
#     name=str(input('enter the name :'))
#     java.add(name)
#     print(java)

# python={'a','b','d','f','g'}
# c=int(input('enter the limit :'))
# for i in range (c):
#     name=str(input('enter the name :'))
#     python.add(name)
#     print(python)
              

    
# php={'a','b','c'}
# java={'a','b','d','e'}
# python={'a','c','f','g'}
# s=php.difference(java).difference(python)
# s1=java.difference(php).difference(python)
# s2=python.difference(java).difference(php)
# # print(s)
# # print(s1)
# # print(s2)
# f=s.union(s1).union(s2)
# print(f)


                #function

# def sample():
#     print('welcome')
#     print('welcome1')
#     print('welcome2')
# sample()
# a=[1,2,3,4,5]
# print(a)
# sample()
# a=[1,2,3,4,5]
# print(a)
# sample()


# def sample ():
#     b=10 #local
#     print('inside function a=',a)
#     print('inside function b=',b)
# a=20     #global
# sample ()
# print('outside function a=',a)
# # print('outside function b=',b)


# def sample ():
#     a=10 #local
#     print('inside function a=',a)
# a=20     #global
# sample ()
# print('outside function a=',a)


# def sample ():
#     a=10
#     b=20
#     return 'welcome',a,b
# c,a1,b1=sample()
# print(a1)
# print(b1)
# print(c)


# def number ():
#     a=int(input('enter a number :'))
#     b=int(input('enter a number :'))
#     return a,b

# while True:
#     print('''
# 1.add
# 2.sub
# 3.mul
# 4.div
# 5.exit
# ''')
#     choice=int(input('enter the choice :'))
#     if choice==1:
#         a,b=number()
#         print(a+b)
#     elif choice==2:
#         a,b=number()
#         print(a-b)
#     elif choice==3:
#         a,b=number()
#         print(a*b)
#     elif choice==4:
#         a,b=number()
#         print(a/b)
#     else:
#         break


# def number ():
#     a=int(input('enter a number :'))
#     b=int(input('enter a number :'))
#     return a,b
# def add():
#     a,b=number()
#     print(a+b)
# def sub():
#     a,b=number()
#     print(a-b)
# def mul():
#     a,b=number()
#     print(a*b)
# def div():
#     a,b=number()
#     print(a/b)

# while True:
#     print('''
# 1.add
# 2.sub
# 3.mul
# 4.div
# 5.exit
# ''')
#     choice=int(input('enter the choice :'))
#     if choice==1:
#         add()
#     elif choice==2:
#         sub()
#     elif choice==3:
#         mul()
#     elif choice==4:
#         div()
#     else:
#         break



# def sample (a,b):
#     print(a,b)
# sample (10,20)
# sample('asd',20)
# sample(['asd',20,21]20,20)


# def sample(name='abc',age=20):
#     print(name,age)

#sample()
# sample('fayas',22)
# sample('fayas')
# sample(22)


# def sample(*a):
#     print(a)

# sample()
# sample('hello','welcome',12,3,4,5.3)


# def sample(**a):
#     print(a)
    
# sample()
# sample(name='fayas',age=22)












# emp=[{'id':1,'name':'fayas','salary':20000,'dob':'1/9/2002','pos':'manager','password':'1/9/2002'}]
# def login():
#     uname=input('enter uname')
#     passw=input('enter passw')
#     f=0
#     if uname == 'admin' and passw == 'admin':
#         f=1
#     user=''
#     for i in emp:
#         if uname.isdigit():
#             uname=int(uname)
#             if uname==i['id'] and passw==i['password']:
#                 f=2
#                 user=i
#     return f,user

# def add_emp():
#     id=int(input('enter the id :'))
#     f1=0
#     for i in emp:
#         if i['id']==id:
#             f1=1
#             add_emp()
#     if f1==0:
#         name=str(input('enter the name :'))
#         salary=int(input('enter the salary'))
#         dob=str(input('enter dob :'))
#         pos=str(input('enter the pos :'))
#         password=dob
#         emp.append({'id':id,'name':name,'salary':salary,'dob':dob,'pos':pos,'password':password})


# def view_emp():
#     print(emp)

# def update_emp():
#     id=int(input('enter id :'))
#     f1=0
#     for i in emp:
#         if i['id']==id:
#             f1=1
#             salary=int(input('enter salary :'))
#             pos=str(input('enter position :'))
#             i['salary']=salary
#             i['pos']=pos

#     if f1==0:
#         print('invalid id')

# def delete_emp():
#     id=int(input('enter id :'))
#     f1=0
#     for i in emp:
#         if i['id']==id:
#             f1=1
#             emp.remove(i)

#     if f1==0:
#         print('invalid id')


# def profile(user):
#     print(user)

# def update_profile(user):
#     name=str(input('enter name'))
#     dob=str(input('enter dob'))
#     user['name']=name
#     user['dob']=dob


# while True:
#     print('''
# 1.login
# 2.exit
#     ''')
#     ch=int(input('enter the choice :'))
#     if ch==1:
#         f,user=login()
#         # f=login()
#         if f==1:
#             while True:
#                 print('''
#                 1.add emp
#                 2.view
#                 3.update
#                 4.delete
#                 5.logout
#                 ''')
#                 sub_ch=int(input('enter the choice :'))
#                 if sub_ch==1:
#                     add_emp()

#                 elif sub_ch==2:
#                     view_emp()

#                 elif sub_ch==3:
#                     update_emp()

#                 elif sub_ch==4:
#                     delete_emp()

#                 elif sub_ch==5:
#                     break

#         elif f==2:
#             if user['dob']==user['password']:
#                 password=input('enter new password')
#                 user['password']=password


#             while True:
#                 print('''
# 1.view profile
# 2.update profile
# 3.logout
# ''')
#                 sub_ch=int(input('enter a choice'))
#                 if sub_ch==1:
#                     profile(user)
#                 elif sub_ch==2:
#                     update_profile(user)
#                 elif sub_ch==3:
#                     break


#         else:
#             print('invalid uname and passw')

#     elif ch==2:
#         break
#     else:
#         print('invalid choice')     


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# user=[{'name': 'aaa', 'id': 101, 'email': 'a@', 'books': [201,202], 'phone': 123, 'password': 'asd'}]
# lib=[{'name':'balarama','id':201,'price':25,'stock':10},{'name':'balarama','id':202,'price':25,'stock':10}]

# def register():
#     if len(user)==0:
#         id=101
#     else:
#         id=user[-1]['id']+1
    
#     email=str(input('enter email :'))
#     f1=0
#     for i in user:
#             if i['email']==email:
#                 f1=1
#                 register()
#     if f1==0:
#             name=str(input('enter the name :'))
#             username=email
#             phone=int(input('enter phone no :'))
#             password=input('enter the password :')
#             user.append({'name':name,'id':id,'email':email,'books':[],'phone':phone,'password':password})


# def login():
#     uname=input('enter uname')
#     passw=input('enter passw')
#     f=0
#     if uname=='admin' and passw=='admin':
#         f=1
#     log=''
#     for i in user:
#         if uname==i['email'] and passw==i['password']:
#             f=2
#             log=i
#     return f,log   


# def add_book():
#     if len(lib)==0:
#         id=201
#     else:
#         id=lib[-1]['id']+1
#     f1=0
#     for i in lib:
#         if i['id']==id:
#             f1=1
#             add_book()
#     if f1==0:
#         name=str(input('enter the name :'))
#         price=int(input('enter the price :'))
#         stock=int(input('enter the stock'))
#         lib.append({'name':name,'id':id,'price':price,'stock':stock})


# def view_book():
#     for i in lib:
#         print(i)


# def update_book():
#     id=int(input('enter id :'))                                                         
#     f1=0
#     for i in lib:
#         if i['id']==id:
#             f1=1
#             price=int(input('enter price :'))                                   
#             stock=str(input('enter stock :'))
#             i['price']=price
#             i['stock']=stock
#     if f1==0:
#         print('invalid id')



# def delete():
#     id=int(input('enter id :'))
#     f1=0
#     for i in lib:
#         if i['id']==id:
#             f1=1
#             lib.remove(i)

#     if f1==0:
#         print('invalid id')


# def view_user():
#     for i in  user:
#         print('name',i['name'])
#         print('id',i['id'])
#         print('email',i['email'])
#         print('phone',i['phone'])




# def view_profile(log):
#     print(log)


# def update_profile(log):

#     name=str(input('enter name :'))
#     phone=int(input('enter phone :'))
#     log['name']=name
#     log['phone']=phone
  


# def lend_book(log):
#     id=int(input('enter id :'))
#     f=0
#     for i in lib:
#         if i['id']==id:
#             f=1
#             i['stock']-=1
#             log['books'].append(id)
#             print('book added')
#     if f==0:
#         print('invalid id')


# def return_book(log):
#     id=int(input('enter id :'))
#     f=0
#     for i in lib:
#         if i['id']==id and id in log['books']:
#             f=1
#             i['stock']+=1
#             log['books'].remove(id)
#             print('book returned')
#     if f==0:
#         print('invalid id')



# def book_in_hand(log):
#     print(log['books'])





# while True:
#     print('''
# 1.register
# 2.login
# 3.exit
#     ''')
#     choice=int(input('enter the choice'))
#     if choice==1:
#         register()
#     elif choice==2:
#         f,log=login()

#         if f==1:
#             while True:
#                 print('''
#                 1.add book
#                 2.view book
#                 3.update book
#                 4.delete
#                 5.view user
#                 6.exit
#                 ''')
#                 sub_ch=int(input('enter the choice :'))
#                 if sub_ch==1:
#                     add_book()
#                 elif sub_ch==2:
#                     view_book()
#                 elif sub_ch==3:
#                     update_book()
#                 elif sub_ch==4:
#                     delete()
#                 elif sub_ch==5:
#                     view_user()
#                 elif sub_ch==6:
#                     break

#         elif f==2:
#             while True:
#                 print('''
#                 1.view profile
#                 2.view book
#                 3.update profile
#                 4.lend book
#                 5.return book
#                 6.book in hand
#                 7.exit
#                 ''')
#                 sub_ch=int(input('enter the choice :'))
#                 if sub_ch==1:
#                     view_profile(log)
#                 elif sub_ch==2:
#                     view_book()
#                 elif sub_ch==3:
#                     update_profile(log)
#                 elif sub_ch==4:
#                     lend_book(log)
#                 elif sub_ch==5:
#                     return_book(log)
#                 elif sub_ch==6:
#                     book_in_hand(log)
#                 elif sub_ch==7:
#                     break


#         elif f==0:
#             print('invalid uname or passw')
#     elif choice==3:
#         break
#     else:
#         print('invalid')
 



 


 # data=lambda a,b: a+b
# print(data(10,5))

# l=[1,2,3,4,5,6,7,8]
# print(list(filter(lambda x:x%2!=0,l)))

# def num(x):
#     return x%2==0
# print(list(filter(num,l)))



# l=['hello','welcome','apple','kiwi']
# print(list(filter(lambda x:'e' in x,l)))


#MAP

# l=[1,2,3,4,5,6,7]
# print(list(map(lambda x:x+10,l)))

# def num(x):
#     return x+10
# print(list(map(num,l)))


def sample():
    print('hello')
sample()

a=10