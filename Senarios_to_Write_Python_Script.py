#1-----------------------------------------------------

#print("Hello Univision")

#2-------------------------------------------------------

#join two string

# string1 = "Balkumar"
# string2 = " Sharma"
# joined_string = string1 + string2
# print(joined_string)
#3------------------------------------------------------------
#Format floating point in the string:

# Use of String Formatting
# float1 = 563.78453
# print("{:5.2f}".format(float1))
#
# # Use of String Interpolation
# float2 = 563.78453
# print("%5.2f" % float2)
#

#4-------------------------------------------------------

# import math
# # Assign values to x and n
# x = 4
# n = 3
#
# # Method 1
# power = x ** n
# print("%d to the power %d is %d" % (x,n,power))
#
# # Method 2
# power = pow(x,n)
# print("%d to the power %d is %d" % (x,n,power))
#
# # Method 3
# power = math.pow(2,6.5)
# print("%d to the power %d is %5.2f" % (x,n,power))

#5----------------------------------------------
# # Assign a numeric value
# number = 70
#
# # Check the is more than 70 or not
# if (number >= 70):
#     print("You have passed")
# else:
#     print("You have not passed")

#6-----------------------------------------------------
# Switcher for implementing switch case options
def employee_details(ID):
    switcher = {
        "1004": "Employee Name: MD. Mehrab",
        "1009": "Employee Name: Mita Rahman",
        "1010": "Employee Name: Sakib Al Hasan",
    }
    '''The first argument will be returned if the match found and
        nothing will be returned if no match found'''
    return switcher.get(ID, "nothing")

# Take the employee ID
ID = input("Enter the employee ID: ")
# Print the output
print(employee_details(ID))