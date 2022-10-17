""" Print the following pattern using for loop
   5 4 3 2 1
   4 3 2 1
   3 2 1
   2 1
   1"""
numbers =int(input("Enter the number:\n"))
for i in range(-numbers,1):
    for j in range(i-1):
        print("* ",end="")
    print(" ")


#############################################################

#Given a number count the total number of digits in a number
# num = 123456
# count = 0
# #print(len(str(num)))# 1st method
# while num !=0 :
#     num//=10
#     count+=1
# print(str(count))





#######################################################################
#Print multiplication table of a given number
# numbers = int(input("Enter the number:\n"))
# print("Table of given number:\n")
# for num in range(1,11):
#     num1 = numbers *num
#     print(num1)


#####################################################################
#Accept number from user and calculate the sum of all number from 1 to a given number
# number = int(input("Enter the number: \n"))
# sum = 0
# for i in range(number+1):
#     sum += i
# print(sum)


###################################################

"""Print the following patterns
   1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5"""

# num = int(input("Enter the number:\n"))
# for i in range(num):
#     for j in range(1,i+2):
#         print(j,end=" ")
#     print(" ")


###############################################################################

#Given a list of numbers, return True if first and last number of a list is same

# num =[10,22,30,40,50,40,10,12]
# #for num in range(len(list1)):
# if num[0] == num[-1] :
#     print("first and last  number is same")
# else:
#     print("first and last number is not same ")
#
#

#######################################################################################

#Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
# str1= input("Enter the strings:\n")
# n = 5
# res = ''
# for i in range(0, len(str1)):
#     if i>= n:
#         res = res + str1[i]
# print(res)





########################################################################################

#Given a string, display only those characters which are present at an even index number.
# str1 = "Balkumar Vishwakarma"
# # print(str1[::2]) # 1st method
# even = []
# for i in range(len(str1)):
#     if i % 2 == 0:
#         even.append(str1[i])
# print("Even characters: {}".format(even))



########################################################################
#Find the greatest of 3 numbers
""""
num1 =int(input("Enter the first number:\n"))
num2 =int(input("Enter the second number:\n"))
num3 =int(input("Enter the third number:\n"))

if num1>num2 :
    print("largest number:",num1)
elif+
 num2>num3:
    print("largest number:",num2)
else:
    print("largest number:",num3)

"""

#####################################################################
# import turtle
# colors = ["red","purple","green","yellow","blue","black","orange"]
# t = turtle.Pen()
# turtle.bgcolor("white") # graphical color page where we could draw image
# for x in range(360):
#     t.pencolor(colors[x%len(colors)])
#     t.width(x//100 + 10) #thickness of pen
#     t.forward(x)
#     t.left(45) # size of pen to turn left and right
