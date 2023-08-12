#How to Sort List Of Tuples By The First Element

#Using Sort() function
# lang_listtuple= [('C#',1), ('Go',7), ('Basic',8), ('Python',60)]
# print('original list of tuples =\n',lang_listtuple)
# lang_listtuple.sort()
# print('after sorting =\n',lang_listtuple)


#----------------------------------------------------
#How to Sort List Of Tuples By Second Element

# lang_listtuple= [('C#',1), ('Go',7), ('Basic',8), ('Python',60)]
# print('original list of tuples =\n',lang_listtuple)
# lang_listtuple.sort(key = lambda item:item[1])
# print('after sorting by second item=\n',lang_listtuple)

#-----------------------------------------  ------
# How to remove duplicate from list of tuples
# Using List comprehension

#a list of tuples
# list_of_tuples= [("C#", 1), ("C#", 1), ("C++", 3), ("C++", 3), ("Python", 25), ("Rust", 30)]
# #removing the duplicate
# unique_list_of_tuples=list(set([item for item in list_of_tuples]))
# print('list of tuple after removing duplicate=\n', unique_list_of_tuples)

#---------------------------------------------
#How to remove duplicate from list of tuples using dict() function

listofTuples = [("C#" , 2), ("JS" , 3), ("C#" , 2),("GO" , 23),("Java" , 77)]
dictiwithlistof_tuples = dict(listofTuples)
print(dictiwithlistof_tuples)

#------------------------------------------------------
#How do we reverse a string in Python?

# String = "String Example" [::-1]
# print(String)

#---------------------------------------------
# convert list to tuple.

# listelements = ['C#', 'Java', 'Go', 'Rust']
# tuple = tuple(listelements)
# print(tuple)

#--------------------------------------
#How to convert two list to dictionary in Python?

# Subj = ["Math", "English", "computer", "Music"]
# marks = [98, 90, 75, 100]
# student_score = dict(zip(Subj, marks))
# print(student_score)


#-----------------------------------------------
#How To Filter A List of Given Elements In a List Of Tuples?

#Using lambda and list

# listoftuple = [(1,2,'C#'),('Pyth',4),('Pyth',5,6),(7,8,),('Pyth',6)]
# item = 'Pyth'
# output = list(filter(lambda x:item in x, listoftuple))
# #filltering the list of tuple
# print('fliterring list of tuples =\n',output)

#--------------------------------------------------
#Different Ways To Concatenate Tuples In Python.
# tupleint= (1,2,3,4,5,6)
# langtuple = ('C#','C++','Python','Go')
# #concatenate the tuple
# tuples_concatenate = sum((tupleint, langtuple), ())
# print('concatenate of tuples \n =',tuples_concatenate)

#---------------------------------------------
#Sum() to concatenate tuple into a nested tuple

# tupleint= (1,2,3,4,5,6),
# langtuple = ('C#','C++','Python','Go'),
# #concatenate the tuple
# tuples_concatenate = sum((tupleint, langtuple), ())
# print('concatenate of tuples \n =',tuples_concatenate)

#--------------------------------------------------------------
#Write a program to create mixed datatype tuple in Python

# Langtuple = (1, "C#", 3.4,'C++',False,True)
# print('mixed type tuple=',Langtuple)

#--------------------------------------------------------------------------
#What will be the output of tuple slicing program .

# Langtuple = (1, "C#", 3.4,'C++',False,True)
# print( Langtuple[::5])
# print( Langtuple[::2])
# print( Langtuple[:-3])

#------------------------------------------------------------------------
#How to replace the last tuple value from list of tuples.

# listoftuple = [(1, "C#",40), (3.4,'C++',False),(True,0,56)]
# print([tuple[:-1] + (45,) for tuple in listoftuple])

#------------------------------------------------------------------------------
#How to remove empty tuple from list of tuples.

# listoftuple = [(1, "C#",40),(),('',),(3.4,'C++',False),(True,0,56),()]
# print([tuple for tuple in listoftuple if tuple])

#-------------------------------------------------------------------------------
#How to convert list of tuple to dictionary

#defining an empty dictionary
# lang_dictionary = {}
# lang_tuples= [("C#", 1), ("C", 2), ("C++", 3), ("Go", 20), ("Python", 25), ("Rust", 30)]
# for lang,value in lang_tuples: #list of tuples to dictionary
#     lang_dictionary.setdefault(lang, []).append(value)
# print('list of tuples to dictionary=\n', lang_dictionary)

#----------------------------------------------------------------------
#How to sort the tuple by float value from list of tuples in ascending order.

# listoftuple = [('C#', '10.20'), ('Go', '13.06'),('F#','10.05'), ('Python', '15.5')]
# print( sorted(listoftuple, key=lambda ele: float(ele[1])))

#--------------------------------------------------------------------------------------
#Write code to unzip a list of tuple in separate lists

# listoftuple = [('C#', '10.20'), ('Go', '13.06'),('F#','10.05'), ('Python', '15.5')]
# print(list(zip(*listoftuple)))

#--------------------------------------------------------
#How to find a Tuple element by value in Python

# tuple = ('C#', 10, 'Go', '13.06','F#','10.05','Python', '15.5')
# item =10
# if item in tuple:
#     print("Element in Tuple")
# else:
#     print("Element not in Tuple")

#--------------------------------------------------------
#Code to find the positive elements tuple from the list of Tuples

# list_of_tuples = [(12, 3, 10), (-15, 6, 9), (-7, 2, 7)] # all() method to check each item of listoftuples
# res = [pos for pos in list_of_tuples if all(item >= 0 for item in pos)] # result
# print("Tuples contain positive items : " ,res)

#------------------------------------------------------------------
#How To Do The Position Sum Of Python Tuple Elements?

# numtuple = (5, 6, 7)
# inttuples = (8, 9, 10,11) # printing both tuples
# print('num tuple =', numtuple)
# print("langtuple : ",inttuples) # tuple using map() and lambda
# added_tuples = tuple(map(lambda num, num1: num + num1, numtuple, inttuples))
# print("tuples addition using map and lambda =" ,added_tuples)

#-------------------------------------------------------------------------
#How to find a tuple that has all elements divide by any number from a list of tuples.

# list_of_tuples = [(12, 8, 16), (24, 16, 28), (7, 2, 7)]
# number = 4 # all() method to check each item of listoftuples
# res = [div for div in list_of_tuples if all(item%number == 0 for item in div)]
# print("Tuple which all items divide by number 4 = : ",res)

#---------------------------------------------------------------------------------
#How to Convert Tuple to string.

# str_tuple = ('This', 'is', 'tuple', 'to', 'string')
# tuple_to_string = ''.join(str_tuple)
# print(tuple_to_string)

#----------------------------------------------------------------------
#Program to remove duplicate from List of Tuples

# lst_of_tuple= [('C#', 1), ('JS', 2), ('C#', 1), ('JS', 2),('React',1)]
# result = [tup for tup in (set(tuple(ele) for ele in lst_of_tuple))]
# print(result)

#------------------------------------------------------------------------
#How to find the Duplicate tuple in list of tuple

# lst_of_tuple= [('C#', 1), ('JS', 2), ('C#', 1), ('JS', 2),('React',1)] #finding the duplicate tuple
# result_tuple = list(set([item for item in lst_of_tuple if lst_of_tuple.count(item) > 1]))
# print(result_tuple)

#----------------------------------------------------------------------------
#How to get the max value tuple from List of Tuple.
# from operator import itemgetter
# lst_of_tuple= [('C#', 100), ('JS', 200),('React',400)] #fmax value tuple key
# result_tuple = max(lst_of_tuple, key = itemgetter(1))[0]
# print(result_tuple)

#---------------------------------------------------------------------------
#How to get min and max key-value pair from the list of Tuples.

# lst_of_tuple= [('C#', 100), ('JS', 200),('React',400)] #key - value with max ,min value
# max_key_value = max(lst_of_tuple)[0], max(lst_of_tuple)[1]
# min_key_value = min(lst_of_tuple)[0],min(lst_of_tuple)[1]
# print(max_key_value,min_key_value)

#---------------------------------------------------------
#Program to generate random number in Python

# import random #Generate random number between 0and 9
# print(random.randint(0,9))

#-------------------------------------------------------------
# import random # choice() function to generate function from list
# print ("Generate number num from list : ")
# print (random.choice([1, 4, 8, 10, 3]))
