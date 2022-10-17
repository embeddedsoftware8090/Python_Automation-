#Write a program to swap two numbers

number1 = float(input("Enter the first number1:\n"))
number2 = float(input("Enter the second number2:\n"))
print("Before the swapping ",number1, number2)
number1,number2 = number2,number1
print("After  the swapping ",number1, number2)