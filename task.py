#a="banana"
#print(a.upper())
#print(a)

#
# 2
#n=[1,2,3,4,5]
#print(5 in n)

#3
#a=int(input("Enter first number:"))
#b=int(input("Enter second number:"))
#c=int(input("Enter third number:"))
#if(a<b and a<c):
      #print(".a is smallest")
#elif(b<a and b<c):
#    print('b is smallest.")
#else:
#     print("c is smallest")

#4
#p=int(input("Enter a three digit number:"))
#a=p//100
#b=p//10%10
#c=p%10
#print(a+b+c)

#5
#x=int(input("Enter the month:"))
#if (x==1):
#    print("January")
#elif(x==2):
#    print("Feburary"))
#elif(x==3):
#    print("March")
#if(x==4):
#   print("April")
#elif(x==5)
#    print("May")
#elif(x==6)
#    print("June")
#elif(x==7)
#    print("July")
#elif(x==8)
#    print("August")
#elif(x==9)
#    print("September")
#elif(x==10)
#    print("October")
#elif(x==11)
#    print("November")
#elif(x==12)
#6
#x=5
#x++3
#print(x)

#7.







#8.
#marks=int(input("Enter marks of students:"))
#if(marks<25):
#   print("F")
#elif(marks>+25 and marks<45):
#    print("E")
#elif(marks>=45 and marks<50):
#    print("D")
#elif(marks>=50 and marks<60):
#    print("C")
#elif(marks>+60 and marks<=80):
#    print("B")
#elif(marks>80):
#    print("A")
#else:
#     print("wrong marks")

#9.
#age=int(input("Enter age of a person:"))
#if(age>=18):
#     print("Adult")
#elif(age>=13):
#    print("Teenager")

#10.
#age=int(input("Enter age of a person:"))
#if age>=18:
#    print("Person is eligible for voting.")
#else:
#    print("Person is not eligible for voting.")


#11.
#number=int(input("Enter a number:"))
#if number%7==0:
#    print("Number is not divisible by 7.")

#12.
#number=int(input("Enter a number:"))
#if(number%2==0):
#    print("Number is even.")
#else:
#    print("Number is odd.")


#13.
#number=int(input("Enter a number:"))
#if number%5==0:
#   print("Hello")
#else:
#    print("Bye!")

#14.
#marksd=int(input("Enter percentage of a student:"))
#if marks>90:
#   print("A")
#elif marks>80 and marks<=90:
#    print("B")
#elif marks>60 and marks<=80:
#    print("C")
#else:
#     print("D")


#15.
#city=input("Enter city name:")
#if city=='Dehli':
#   print("Red fort")
#elif city=='Agra':
#     print("Taj Mahal")
#elif city=='Jaipur':
#     prinjt("Jal Mahal")
#else:
#     print("out of India")

#16.
#a=9
#if a>5 and a<=10:                #hello
#     print("hello")
#else:
#     print("Bye")

#17.
#a=int(input("Enter number:"))
#if a%2==0 and a%3==0:
#   print("Number is divisible by both 2 and 3.")
#else:
#     print("Number is not divisible by 2 and 3.")


#18.
#letter=input("Enter a letter:")
#if letter=='a'
#    print("vowel")
#elif letter=='e'
#     print("vowel")
#elif letter=='i':
#    print("vowel")
#elif letter=='o':
#     print("vowel")
#elif letter=='u':
#     print("vowel")
#else:
#    print("consonant")

#19.
#a=int(input("Enter first number:"))
#b=int(input("Enter second number:"))
#c=input("Enter mathematical operator:")
#if(c=='+'):
#   print(a+b)
#elif(c== '-'):
#    print(a-b)
#elif(c=='*'):
#    print(a*b)

#for i in range(1,101):
#      print("python")

#for i in range(10):
#      print(f"hello{i}")


#for i in range(10):
#      print("Hello world")
#print("Hi Ram")

#a="python"
#for i in range(5):
#     print(a)

#for i in range(1,52):
#      print(i)

#a="python"
#for i in a
#      print(i)

#a="python"
#for i in range(0,5):
#      print(i,"=" a,[i])


#a="programming"
#for i in range(1,12):
#      print(i,"=" a,[i])
#else:
#      print("python")

#a=2
#for i in range(11):
#      print(a,"*",i,"=",a*1)

#a=2
#for i in range(10,0,-1):
#    print(a,"*",i,"=",a*i)


#='Python'
#for i in range(5,-1,-1):
#      print(a[i],end="")

#nal_origninal_list=[1,2,3]
#reversed_list=[ ]
#for i in reversed(orignilist):
#      reversed_list.append(i)
#print(reversed_list) 

#a=[5,4,8,9,10,12]
#sum=0
#for i in a:
#      sum=sum+i
#print(sum)    

#b=[5,4,9,8,9]
#mul=1
#for i in b:
#      mul=mul*i
#print(mul)

#n=int(input("enter any positive number:"))
#if n>1:
#      for i in range(2,n):
#            if n%i==0:
#                  print("not prime")
#                  break
#      else:
#            print("prime number")

#username=input("Ente username:")
#password=input("Enter password:")
#for i in range(0,3):
#      print("Enter your credentials")
#      username1=input("Enter your username:")
#      password1=input("Enter your password:")
#      if username==username1 and password==password1:
#            print("You are successfully logged.")
#            break
#      else:
#            if(username!=username1 or password!=password1):
#                  print("Invalid credentials")
#else:
#      print("3 attempt finished")

#for i in range(2):



# *****
# ****
# ***
# **
# *


# row=int(input("Enter number of rows:"))
# for i in range(row):
#       for j in range(row-i):
#             print("*",end="")
#       print("\r")


# *
# **
# ***
# ****
# *****

# row=int(input("Enter number of rows"))
# for i in range (0,row):
#       for j in range (0,i+1):
#             print("* ",end="")
#       print("\r")

# *****
# *****
# *****
# *****
# *****
# row=int(input("Enter number of rows:"))
# for i in range(row):
#       for j in range (row-1):
#             print("*",end="")
#       print("\r")


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# 


# if 5<2:
#       pass
# else:
#       print("Else part")
# print("Rest of the code")
            
      
# =10
# b=2
# while(a>=1):
#       print(b,"*",a,"=",b*a)
#       a=a-1


# a=[1,2,3,4]a
# sum=0
# i=0
# lists=len(a)
# while i<lists:
#       sum=sum+a[i]
#       i=i+1
# print(sum)

# a=[9,8,7,6]
# list[]
# i=


# ch=input("Enter the Alphabet:")
# if ch in('a,''e','i','o','u'):
#       print(ch,"is a vowel")
# else:
#       print("ch,is a consonant")


# vowel=[a,e,i,o,u]
# vowel=input("Enter a alphabet letter:")
# for i in vowel:
#       while vowel==i:
#             i=i+1
#             break


# while(1==1):
#       print("python")
#       break
# else:
#       print("hi")
# print("rest")


# while a<=5:
#       print(a)
#       a+=1
# else:
#       print("while c else part executed")
# print("Rest of the code")

# i=1
# while i<=10:
#       print(i)

# i=1
# while true:
#       print("Python")
#       i=i+1
#       if i==5:
#       break


# i=0
# while True:
#       i+=1
#       print(i)
#       if(i==3):
#             break
# print("Rest of the code")


# i=1
# while i<=10:
#       if i==5:
#             break
#       print(i)
#       i=i+1
#       print("Hello")

# i=1
# while i<=9:
#       if i==8:
#             continue
#       print(i)

# add():
#       x=10
#       y=20
#       c=x+y
#       print(c)
# add()def 


# def login(username,password):
#       print(f"Your username is:{username} and your {password}")
# login("sunil","Battle")
  
 
# def login(username,email,address,number,password):
#       print(f"Your username is:{username}.Your email is:{email}.Your address is:{address}.Your number is:{number}.Your password is:{password}")
#       login("sunil","sunil12","9848780325","dillibazar","battle")


# def operation(x,y):
#       a=x+y
#       b=x-y
#       c=x*y
#       d=x%y
#       print(f"The sum is {a}"."The difference is{b}"."The mul is {c}"."The remainder is {d}")
#       login("a","b","C","d")

 


# def operation(x,y,z):
#       if x>y and x>z:
#             print(x)
#       elif y>x and y>z:
#             print(y)
#       else:
#             print(z)
# operation(30,20,10)

# a=[1,2,3,4]
# sum=0
# for i in a:
#       sum=sum+i
# print(sum)

# def add():
#       a=[1,2,3,4]
# sum=0
# for i in a:
#       sum=sum+i
# print(sum)
# add()

# a=[1,2,3,4]
# mul=1
# for i in a:
#       mul=mul*i
#       print(mul)

# def mul():
#       a=[1,2,3,4]
# mul=1
# for i in a:
#       mul=mul*i
#       print(mul)
# add()


# _st) origninal_list=[8,9,10,11]
# reversed_list=[ ]
# for i in reversed(_origninal_list):
#       reversed_list.append(i)
# print(reversed_li

# def show(name,age):
#       print(f"Name:{name} Age:{age}")
# show(name="Sunil",age=20)


# def show(*num):
#       z=num[0]+num[1]+num[2]
#       print(z)
# show(5,4,3)


# c=3)def show(**num):
#       z=num['a']+num['b']+num['c']
#       print(z)
# show(a=5,b=4,


# y=10
# def outer():
#       z=4
#       def inner():
#             x=4
#             print(x)
#             print("inside the function y,"y)
#       inner()
#       print("z:",z)
# outer()
      

# y=10
# def outer():
#       z=4
#       def inner():
#             x=4
#             z=z+1
#             print(x)
#             print("inside the function y",y)
#       inner()
#       print("z":,z)
# outer()


# y=10
# def outer():
#       x=4
#       def inner():
#       x=8
#       print(x)
#       inner()
# outer()


# def outer():
#       x="local"
#       def inner():
#             nonlocal x
#             x="nonlocal"
#             print("inner:",x)
#       inner()um
#       print("outer:",x)
# outer()

# result=lambda n1,n2,n3: n1+n2+n3
# print("sum of three values:",result(10,20,25))

# result=lambda a1,a2,a3: (a1+a2+a3,a1-a2-a3,a1*a2*a3,a1/a2/a3)
# print(result(2,5,6))






# li=[5,7,22,97,54,62,77,23,73,61]
# square_list=list(map(lambda x:x**2,li))
# print(square_list)
 
# a=[1,2,3]
# b=[3,4,5]
# abc=list(map(lambda x,y:x+y,a,b))
# print(abc)




# data=[1,2,3,4,5,5,6,6,7,9,10]
# var=list(filter(lambda x:x%2==0,data))
# print(var)

# from functools import reduce
# li=[5,8,10,20,50,100]
# sum=reduce((lambda x,y:x+y),li)
# print(sum)



# Create a function with variable length of arguments.

# def myfun(*argy):
#       for arg in argv:
#             print(arg)
# myFun('Hola','Welcome','to','SSIT')


# 2.Create an inner function to calculate the addition in the following way.

# def outer(a,b):
#       x=a**2
#       def ine(a,b)
#       return a+b
#       add=ine(a,b)
#       return add+5
# result=outer(12,12)
# print(result)

from ast import Yield
import numbers
from tkinter import Y
from typing import Tuple
from unicodedata import name


# 3. Assin a difference name to functionand call it trough the new name
#    Below is the function display_student(name,age).
#    Assin new name
#    show_tudent(name,age)to it and call it using the new name.

#    def display_student(name,age):
#          print(name,age)
#       display_student('prapti',20)
#       show_tudent=display_student
#       show_tudent('prapti',20)

# 4.Find the largest item from a given list.

# x=[1,2,3,4,5,6,7,8]\

# x=[1,2,3,4,5,6,7,8]
# print(max(x))


# 5.What is the difference between 10/3 and 10//3?

# a=10
# b=3
# print(a/b)
# print(a//b)

# 6.What is the diffwerence between local and global variables?

# local function,the local variable ends when the function ends.
#   global variable are the variable used throughiut the operation.


# 8.write a function called fizz_buzz that takes a number.
# If the number is divisib,e by 3,it should run "fizz".



# def fizz_buzz(input):
#       if(input%3==0:)and(input%5==0):
#             return 'FizzBuzz'
#             if input%3==0:
#                   return 'Fizz'
#                   if input%5==0:
#                         return 'Buzz'
#                         return input
#             print(fizz_buzz(33))
#             print(fizz_buzz(5))


# 9.

# sp=int(input('enter the speed acquired by the driver;')
# if sp<70:
#       print('Ok')
# else:
#       print('warning')


# 10.

# h=int(input('enter a positive number;'))
# for a in range (1,11):
#       print(h,"x",a,'=',h*a)


# 11.
# s=int(input('enter a num;'))
# t=0
# while s>0:
#       c=s%10
#       t=t*10+c
#       s=s//10
# print('the rev of the number is',t)


# 12.
# p="CosmikDebries
# q=0
# for i in range(0,(len(p))):
#       if p[i]!="":
#             q=q+1
# print('total characters on a string is:'+str(q))

# 13.
# def mul():
#       list=[8,2,3,-1,7]
#       list=1
#       for i in range (0,5):
#             ist=list[i]+ist
#       print(list)
# mul()

14.

def add():
      a=[8,2,3,0,7]
      b=0
      for i in range(0,5):
            b=a[i]+b
      print(b)
add()

# 15.
# def prinvelndexChar(str):
#       for i in range(0,len(str)-1,2)
#       print("index[',i,"]",str[i])
# inputStr=input("Enter String")
# print("orginal String is ",inputStr)
# print("Printing only even index chars")
# printEvelndexChar(inputStr)

# 16.
# def char(str):
#       for i in range(1,len(str)-2,2):
#             print("index[",i,"]",str[i])
#       inputstr=input('enter a string;')
#       print('original string is',inputstr)
#       print('printing only odd chars')
#       char(inputstr)

# 17.
# a=[1,2,3,4,5,6,7,8,9,10]
# b=0
# for i in range(0,10):
#       b=a[i]=b
# print(b)

# 18.

# def is_even_num(i):
#       enum=[]
#       for n in i:
#             if n%2==0:
#                   enum.append(n)
#                   return enum
#             print(is_even_num([1,2,3,4,5,6,7,8,9,)

# 19.

# list of numbers
# list1=[12,13,14,15,16,17,18,19]
# for num in list1:
#       if num %2!=0:
#             print(num,end=",")

# 20.
# a=int(input('enter your percentage;'))
# if a>=65 and a<=100:
#       print('excellent')
# elif a>55 and a<65:
#       print('good')
# elif a>=41 and a<55:
#       print('fair')
# else:
#       print('failed')


# def add(a,b):
#       print(a+b)
#       add(2,3)

# import a
# a.add(5,6)

# import math


# a=air/math
# print(a)

# import math
# a=20
# print(math.sqrt(a))



#  print(factorial(a))
#  print(math,floor(a))
#  print(math,pow(a))
#  print(math,exp(a,b))
#  print(math,gcd(a,b))

# import _random
# list1=[1,2,3,4,5,6]
# print(random.choice(list1))

# declare a list
# sample_list=[1,2,3,4,5]
# print("Original list:")
# print(sample_list)
      


# import random
# for i in range(50):
#       print(random.radint(20,50))

# import random
# b=[]
# for i in range (50):
#       a=random.radint(1,20)
#       b.appened
#       print(b)

# import datetime
# x=datetime.datetime.now()
# print(x.year)
# print(x.strftime("%



# data={1,2,3,4}
# data.add(5)
# print(data)

# data={1,2,3,4,5}
# data.remove(1)
# print(data)

# a={"lemon","cat","cherry"}
# a.discard("cat")
# print(a)

# data={1,2,3,4,5,6,7,'danish',3.14}
# if 'danish' in data:
#       print('present')
# else:
#       print('Not present')


# data={1,2,3,4,5,6}
# data.clear()
# print(data)


# data1={1,2,3,4,5,6}
# print(data1)
# data2=data1.copy()
# print(data2)

# x={"a","b","c"}
# y={"b","d","f"}
# x.update(y)
# print(x)

# data1={1,2,3,4}
# data2={3,4,,6}
# union_set=data1|data2
# print(union_set)

# data1={1,2,3,4}
# data2={3,4,5,6}
# intersection_set=data1 & data2
# print(intersection_set)

# data={1,2,3,4}
# data2={3,4,5,6}
# difference=data2.difference(data1)
# print(difference)

# a={1,2,3,4}
# b={3,4,5,6}
# disjoint=a.isdisjoint(b)
# print(disjoint)




# my_dict={'name': 'John',1:[2,4,3]}

# data1=dict(Name='Sunil'Rawat',age=17)
# print(data1)

# data={'Name':'Sunil Rawat','Age':17}
# print(data)
# for i in data:
#       print(i)
# for i in data.values():
#       print(i)
# for i in data.items():
#       prinmt(i)

# data={'Name':'Sunil Rawat','Age':17}
# print(data['Name'])
# print(data['Age'])

# data={}
# print(data)
# data['Name']="Sunil Rawat"
# data['Age']=20
# print(data)

# data={'Name':'Sunil Rawat','Age':20}
# if 'Name' in data:
#       print('present')
# else:
#       print('Not present')
# if 'Sunil Rawat' in data.values():
#       print('present')
# else:
#       print('Not present')



# data={'Name':'Sunil Rawat','Age':20}
# data2={'Fav Movie':'3 idiots','Sports':Boxing}
# data.update(data2)
# print(data)


# data={'Name':'Sunil Rawat','Age':20}
# del data["Age"]
# print(data)

# data={'Name':'Danish Ali','Age':17}
# print(data)
# remove_pop=data.pop('Age')
# print(remove_pop)

# data1={'Name':'Sunil Rawat','Age':20}
# get_data=data1.get('Name')
# print(get_data)

# data={'Name':'Sunoil Rawat','Age':20}
# print(data)
# data.clear()
# print(data)

# a_dict={"a":1,"B":2,"C":3}
# new_key="A"
# old_Key="a"
# a_dict[new_Key]=a_dict.pop(old_key)
# print(a_dict)


# def login():
#       print("Something went wrong")
#       login()



# x=10
# c=x+Yield
# print(c)


#Task 7 week 5

#1.

# a = [18, 52, 23, 41, 32]
# smallest = min(a)
# print(f'Smallest number in the list is : {smallest}.')
 
#2.

# a = ["Hire", "the", "top", "1%", "freelancers"]

# b = []

# if a:
#     print("list is not empty")
# else:
#     print("list is empty")

#4.
# prime_numbers = [2, 3, 5]
# numbers = prime_numbers.copy()
# print('Copied List:', numbers)

#5.

# Python program to find second largest number
# in a list
 
# list1 = [10, 20, 4, 45, 99]
# new_list = set(list1)
# new_list.remove(max(new_list))
# print(max(new_list))

#8.
# intTuple = ()
# number = int(input("Enter the Total Number of Tuple Items = "))
# for i in range(1, number + 1):
#     value = int(input("Enter the %d Tuple value = " %i))
#     intTuple = intTuple + (value,)    
# print("Tuple Items = ", intTuple)

# #9.
# aTuple = (True, 28, 'Tiger')
# aList = list(aTuple)
# print(type(aList))
# print(aList)


#10.

# def convertTuple(tup):
#     st = ''.join(map(str, tup))
#     return st
# tuple = ('g', 'e', 'e', 'k', 's', 101)
# str = convertTuple(tuple)
# print(str)

#11.

# listx = [5, 10, 7, 4, 15, 3]
# print(listx)
# tuplex=tuple(listx)
# print(tuplex)
	 
#12.

# print(list x)
# tuplex=tuple(list x)
# print(tuplex)
# tuples=[('Key1',1),('Key2',2),('key3',3),('Key4',4),('Key5',5)]
# result={}
# for (Key,value)in tuples:
#        result.setdefault(Key,[].append(value))
#        print(result)

#15.

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(x):
#   if x in d:
#       print('Key is present in the dictionary')
#   else:
#       print('Key is not present in the dictionary')
# is_key_present(5)
# is_key_present(9)

# #17.
# dict_1 = {1: 'a', 2: 'b'}
# dict_2 = {2: 'c', 4: 'd'}

# dict_3 = dict_2.copy()
# dict_3.update(dict_1)

# print(dict_3)

#19.

# s1 = {}
# print(s1)

# s2 = set()
# print(s2)

#20.
# num_set = set([0, 1, 2, 3, 4, 5])

# for n in num_set:
#   print(n)

#21.

# color_set = set()
# color_set.add("Red")
# print(color_set)

# color_set.update(["Blue", "Green"])
# print(color_set)

#22.

# num_set = set([0, 1, 3, 4, 5])
# print("Original set:")
# print(num_set)
# num_set.pop()
# print("\nAfter removing the first element from the said set:")
# print(num_set)

#23.

# num_set = set([0, 1, 2, 3, 4, 5])
# print("Original set elements:")
# print(num_set)
# print("\nRemove 0 from the said set:")
# num_set.discard(4)
# print(num_set)
# print("\nRemove 5 from the said set:")
# num_set.discard(5)
# print(num_set)
# print("\nRemove 2 from the said set:")
# num_set.discard(5)
# print(num_set)
# print("\nRemove 7 from the said set:")
# num_set.discard(15)
# print(num_set)

#24.

# setx = set(["green", "blue"])
# sety = set(["blue", "yellow"])
# setz = setx & sety
# print(setz)

