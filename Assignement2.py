# num1 = 10
# num2 = 10
# print(num1 is num2)
# print(id(num1))
# print(id(num2))
"""
Find the Output of the following
    print(5//2)
    print(-5//2)
"""

# print(5//2)
# print(-5//2)


"""

Format the following data using a string.format() method.
   totalMoney = 1000
   quantity = 3
   price = 450
expected output :I have 1000 dollars so I can buy 3 football for 450.00 dollars.

"""

# money = int(input("totalMoney  = "))
# quantity = int(input("quantity = "))
# price = int(input("price = "))

# print("I have {} dollers so I can buy {} football for {} dollers.".format(money,quantity,price))



"""

Display float number with 2 decimal places using print()

"""
# number1 = float(input("Enter the number:\n"))
# print("{:.4f}".format(number1))

# number1 = 7.154327
#
# res = "{:.2f}".format(number1)
#
# print(res)


###################################################################

"""

Ask the user to enter Marks of 3 Subjects and find the percentage
    Enter  Subject1 marks :  89
    Enter Subject2 marks :  38
    Enter Subject3 marks :  68
    Percentage : 65% 
    
"""

# sum1 = 0
# for num in range(0,3):
#     marks = int(input(f"Enter the Marks of Student{num} : "))
#     sum1 += marks
#     percentage  = sum1 /(num+1)
# print("Percentage :",percentage )


#######################################################################
"""
Ask the user to enter marks of 5 students and find the average.
    Enter Marks of Student1 :  89
    Enter Marks of Student2 :  38
    Enter Marks of Student3 :  68
    Enter Marks of Student4 :  29
    Enter Marks of Student5 :  99
    Average Marks           :  64.60 
    
"""
# sum1 = 0
# for num in range(0,5):
#     marks = int(input(f"Enter the Marks of Student{num} : "))
#     sum1 += marks
#     avg = sum1/(num+1)
# print("Average Marks :" ,avg)

################################################################################

"""Check if two tuples point to the same object"""
tuple1 = (10,20,30,40)
tuple2 = (10,20,30,40)
tuple3 = (10,20,30,40)
print(tuple2 is tuple1)
print(id(tuple1))
print(id(tuple2))
print(id(tuple3))
print(tuple3 is tuple2)

##################################################################
"""Check if two lists point to the same object"""
# list1 = [10,20,30,40,50]
# list2 = [10,20,30,40,50]
# list3 = [10,20,30,40,50]
# print(list1 is list2)
# print(list3 == list2)

# x = ["a", "b", "c", "d"]
# y = ["a", "b", "c", "d"]
# print(x is y)
# print(x == y)



############################################################################
"""3. Ask the user to enter two values and find the sum like following
    Enter first value : 3
    Enter Second Value : 7
    The sum of 3 and 4 is 7
    """
# num1 = int(input("Enter the first value  :\n"))
# num2 = int(input("Enter the second value :\n"))
# sum = num2 + num1
# print("sum :{} and {} is {} ".format(num1,num2,sum))

#############################################################################

"""

Ask the user to enter two values and find the sum like following
Enter first value : 3
Enter Second Value : 7
Sum  : 7 

"""

# num1 = int(input("Enter the first value  :\n"))
# num2 = int(input("Enter the second value :\n"))
# sum = num2 + num1
# print("sum :{} and {} is {} ".format(num1,num2,sum))


###################################################################################################
# first_name = input("Enter the first name :\n")
# last_name = input("Enter the last name :\n")
# print(first_name ,  last_name)

