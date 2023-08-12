#Program to find the max, min number from the list user input.

# listlang = []#empty list
# numbers = int(input('enter the number of items in list '))
# for num in range(numbers):
#     item = int(input('Entered number '))
#     listlang.append(item) #add element in list
# print('entered list =',listlang)
# print("Max number = :", max(listlang), "\nMin number :", min(listlang)) #print min or max number
# count the number of digits
# l = 75689
# c = 0
# while (l!=0 ):
#     l =l//10
#     c =c+1
# print(c)


#--------------------------------------------------------------
#2. Code to remove duplicate from list using List comprehension
#1st method
# lstnum = [12, 36, 56, 36, 36, 50, 56, 12]
# unique_lst = []
# l= unique_lst.append(i)
# [ l for i in lstnum if i not in unique_lst]
# print ("unique elements list : " ,unique_lst)

#2nd method--------------------------------------------
# lstnum = [12, 36, 56, 36, 36, 50, 56, 12]
# unique_lst = []
# for x in lstnum:
#     if x not in unique_lst:
#         unique_lst.append(x)
# print("unique elements list:",unique_lst)

#-------------------------------------------------------
#3. Program to find the sum of list elements.

# lstnum = [12, 36, 56, 36, 36, 50, 56, 12]
# sum = 0
# for ele in range(0, len(lstnum)):
#     sum = sum + lstnum[ele]
#     print ("sum of list items: " ,sum)

#-----------------------------------------------------
#4. How to Multiply all the elements of list

# lstnum = [6, 2, 3, 1, 10, 4]
# mutiply =1
# for ele in lstnum:
#     mutiply = mutiply* ele
#     print ("multiplication of list items : " ,mutiply)

#---------------------------------------
#5.Program to generate a number list between two ranges.

# listnum = list(range(1, 7))
# print ("list between two range : " ,listnum)

#---------------------------------------------------------------
#6.How to reverse the List using slice

# listnum = [45,67,12,14,56,87]
# #reverselist =listnum[::-1]
# listnum.reverse()
# print ("reverselist : " ,listnum)

#-----------------------------------------------------
#7.How to flatten a list of lists with a list comprehension

# listnum = [[5,6,7,'C#'], ['C++',2,3]]
# flatten_list = [i for sublist in listnum for i in sublist]
# print('flatten list =',flatten_list)

#------------------------------------------------
#8.How to Intersect two list

# listnum = ['C++',2,3,6,7,5,'C#']
# listnum1 = ['C++',5,6,7,'C#']
# intersect_res = [item for item in listnum if item in listnum1]
# print('intersect of two list =',intersect_res)

#---------------------------------------------
#9.Program to shuffle a list and print

# from random import shuffle
# listnum = ['Rust','go','C++',2,3,6,7,5,'C#']
# shuffle(listnum) #shufling funciton
# print('list after shuffling =',listnum)


#--------------------------------------------------------
#10. Program to convert a list into string

# listlang = ['This','is','list','Code']
# listtostring = ' '.join(listlang)  #join the string
# print('list after shuffling =',listtostring)

#----------------------------------------------------------
#11.How to get the square of each list element between two range
#1st method
# listnum = list(range(3,9))
# list_item_square = [ele ** 2 for ele in listnum]
# print(list_item_square)

#2nd method
# import math
# list1 = [10,20,30,40,50]
# for i in list1:
#     l = math.pow(i,3)
#     print(l)



#-----------------------------------------------
#12. Program to get the difference between two List using comprehension

# lstnum = [15, 78, 4,80]
# lstnum1 = [80, 4, 89,78]
# two_list_differnce = [ele for ele in lstnum if ele not in lstnum1]
# print(two_list_differnce)

#----------------------------------------------
#13. How to count the number of list in list of list.

# lstlng = [[15, 78, 4],['C#',80,7],['Go','Rust','C++'],['Python',12]]
# print('count of list of list = ',len(lstlng))

#----------------------------------------
#14. How to get the first element from each nested list of a list

# lstlng = [[15, 78, 4],['C#',80,7],['Go','Rust','C++'],['Python',12]]
# each_list_element = [item[0] for item in lstlng]
# print('first element of each nested list = ',each_list_element)

#-----------------------------------------------------------------
#15. How to count occurrence of repeated element in list

# from collections import Counter
# lstlng = [15, 18, 14,'C#',18,15,'C#','C++','C++','Python',15,15,15]
# # repeation_of_element = Counter(lstlng)
# # print(repeation_of_element
# l=Counter(lstlng)
# print(l)

#----------------------------------------------------------
#16. How to Filter even values from a list using list comprehension

# lstnum = [12, 18, 14,18,15,6,7,3,9,1]
# even_element_list = [ele for ele in lstnum if ele%2 == 0] #even numbers
# print('even item list =',even_element_list)
#
# # filter odd numbers
# odd_element_list =[element for element in lstnum if element%2 ==1]#odd numbers
# print("odd item list =",odd_element_list)
#----------------------------------------------------------
#17.How to Sort a list of integers in descending order

# lstnum = [12, 18, 14,25,15,6]
# lstnum.sort(reverse=True)
# print('list sorting in descending order =',lstnum)

#-------------------------------------------------------
#18.How to Sort a list of integers in ascending order
#sort() method used to sort the list in ascending order.

# lstnum = [12, 18, 14,25,15,6]
# lstnum.sort()
# print('list sorting in ascending order =',lstnum)


#------------------------------------------------------
#19. How to remove elements in a list before a specific index

# lstnum = [12, 18, 14,25,15,6]
# new_list = lstnum[4:]
# print('removing element before specific Index =' ,new_list)

#-------------------------------------------
#20.How to remove empty strings from the list of strings

# liststr = ["Python", "", "list", "first", "", "example"]
# lstafter_remove_empty = list(filter(None, liststr))
# print(lstafter_remove_empty)


#------------------------------------------------------
#21.How to sort two lists simultaneously

# lstnum = [ 5,2, 1, 7,26]
# lstnum1 = [45,35,223, 80, 100]
# lstnum, lstnum1 = zip(*sorted(zip(lstnum, lstnum1)))
# print(lstnum, lstnum1)

#---------------------------------------------------------------
#23.How to concatenate two list element wise/index-wise.

# lststr = ["th", "i", "Pyth", "exa"]
# lststr1 = ["is", "s", "on", "mple"]
# concate_list = [i + j for i, j in zip(lststr, lststr1)]
# print('concatenated list = ',concate_list)

#------------------------------------------------------------
#24. How to concatenate every element across lists using list comprehension

# lststr = ["this", "Python"]
# lststr1 = ["is", "example", "of"]
#
# templst = [(x, y) for x in lststr for y in lststr1]
# concate_list = [x + ' ' + y for (x, y) in templst]
# print('concatenated list = ',concate_list)

#--------------------------------------------------------
#25.How to remove negative values from a list with the filter function

# lstnum = [-5, 27, 1000, -4, 0, -80,56,-67] #Removing negative values
# res_lst = [item for item in lstnum if item >= 0]
# print('list after removing negative values =',res_lst)
#
# import time
# num = 10,20,30,40
# num1= 100,200,300,400
# t =tuple(num)
# l =list(num)
# d =dict(zip(num,num1))
# s =set(num)
# print(t)
# print(l)
# print(s)
# print(d)
#
# time.sleep(5)

#-------------------------------------------------
l1 =[2,4,3]
l2 =[5,6,4]
l3 =[]
var =(l1[0]+l2[0])
var1 =(l1[1]+l2[1])
if l1[1]+l2[1] !=10:
    pass
var2 =(l1[2]+l2[2])
l3.append(var)
l3.append(var1)
l3.append(var2)
print(l3)