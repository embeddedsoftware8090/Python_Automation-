# numbers = 5
# for i in range(numbers):
#     for j in range(numbers):
#         if i == 0: #1st row
#             print("*",end="" )
#         elif j == 0:#1st colom
#             print("*",end="" )
#         elif i == 4: #last row
#             print("*", end="")
#         elif i == 2:#2nd row
#             print("*",end="")
#
#     print("")

#
# str=""
# for Row in range(0,7):
#     for Col in range(0,7):
#         if (Col == 1 or ((Row == 0 or Row == 3 or Row == 6) and (Col < 5 and Col > 1)) or (Col == 5 and (Row != 0 and Row != 3 and Row != 6))) :
#             str=str+"*"
#         else:
#             str=str+" "
#     str=str+"\n"
# print(str)
#----------------------------------------------------------------------
# str1 = "un76i5vi39sio93n11sd32dd42n"
# s =0
# a =0
# c =0
# for ch in str1:
#     if (ch.isdigit()):
#         s = s+int(ch)
#         c = c+1
# print("Sum of the numbers:",s)
# a =s/c
# print("Average of strig:",a)
#---------------------------------------------------------
# str1 = "un!v!$!ene&"
# c =0
# for ch in str1:
#     if (ch.isalpha()):
#         #print("Average of strig:",ch)
#         print(ch)
#     c =c+1
# print(c)
# from threading import Thread
# N = 100000000
# def count(n):
#     while n!=0:
#         n-=1
# count(N)
# def count_thread(n):
#     t1=Thread(target = count,args=(N/2,))
#     t2 = Thread(target=count, args=(N / 2,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
# count_thread()



# import logging
# import threading
# import time
#
# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)
#
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#
#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,))
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     # x.join()
#     logging.info("Main    : all done")
#

# def function2():
#     print("univision")
# def function1():
#     print("Hello")
# function1(),function2()
#----------------------------------------------------------------------------------------

# list1 = [1,2,3,3,45,6,7,8,21]
# list2 = [29,34,53,23,4,7,2,4,32]
# sum = list1 + list2 #concetanation the two list
# print("Concatanation",sum)
# #list1.remove() #remove all the list
# print("Original list :",list1)
# list1.pop()
# print("pop:",list1)
# list1.append(100)
# print("append:",list1)
# list1.sort()
# print("sort:  ",list1)
# print("index",list1.index(6))
# print("Count:",list1.count(3))
# print("Length of list1:",len(list1))
#
# list_dict =dict(zip(list1,list2))
# print("Conversion of two list into dict:",list_dict)
#
#
# #print("Clear:",list1.clear()) #clear all the element in the list
#
# list1_tuple1 =tuple(zip(list1,list2))
# print("COnversion of two list into tuple:",list1_tuple1)
#
# list1_set1 =set(zip(list1,list2))
# print("conversion of two list into set :",list1_set1)
#
#
# def fun(a, b):
#     sum1 = a + b
#     sub = a - b
#     mul = a*b
#     div = a/b
#     return sum1, sub,mul,div



# print(fun(10,20))
#

# def add_without_plus_operator(a, b):
#     while b != 0:
#         data = a & b
#         a = a ^ b
#         b = data << 1
#     return a
# print(add_without_plus_operator(2,10))








#create a function using default argument

# def default(a,b,c,d=10):
#     print(a,b,c,d)
# default(1,2,34)
#
#
#

# str1 = "bjsdk21#(*@)*$&(#jhsd"
#
# for x in str1:
#     if x.isalpha() == False:
#         pass
#     else:
#         print(x)

# def maximum(m):
#     maximum1=m[0] #start  element from zero
#     for i in range(1,len(m)):
#         if(m[i]>maximum1):
#             maximum1=m[i]
#     print(maximum1)
# m=[80,20,30,400,50,400500]
# maximum(m)
#
# print(type(m))  #ssss


# set1 = {10,20,30,40,50,60}
# set2 = {11,20,30,40,55,60}
# res =[x for x in set1 if x in set2]
# print(res)
#
# print(set1.intersection(set2))
# print(a)
# a=set1&set2



# list1 = [1,2,3,4,5]
# sum1 =0
# for x in list1: #for 1,2,3,4
#     sum1+=x
#     if x==4:
#         break
# print("sum of 1st loop=",sum1)
#
# sum1 =0
# for x in list1: #for 2,3,4,5
#     sum1+=x
#     if x==0:
#         continue
# print("sum of 2nd loop =",sum1)

# sum1 =0
# for x in list1: #for 2,3,4,5
#     sum1+=x
#     if x==3:
#         continue
# print("sum of 3rd loop=",sum1)
#
# sum1 =0
# for x in list1: #for 2,3,4,5
#     sum1+=x
#     if x==2:
#         continue
# print("sum of 4th loop=",sum1)
#----------------------------------------------------------
list1 ,list2,sum1= [1,2,3,4,5],[],0
for x in list1:
    if x == 5:
        continue
    list2.append(x)
    sum1+=x
print("list1 =",list2,"sum of 1st loop=",sum1)

#--------------------------------------------------

list1 = [1,2,3,4,5]
list2 = []
sum1 = 0
for x in list1:
    if x == 1:
        continue
    list2.append(x)
    sum1+=x
print(list2)
print("sum of 2nd loop=",sum1)

#------------------------------------------------
list1 = [1,2,3,4,5]
list2 = []
sum1 = 0
for x in list1:
    if x == 2:
        continue
    list2.append(x)
    sum1+=x
print(list2)
print("sum of 3rd loop=",sum1)

#-----------------------------------------------

list1 = [1,2,3,4,5]
list2 = []
sum1 = 0
for x in list1:
    if x == 5:
        continue
    list2.append(x)
    sum1+=x
print(list2)
print("sum of 4th loop=",sum1)

