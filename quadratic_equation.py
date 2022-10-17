#Write a program to solve quadriatic equation

number = float(input("Enter the number of x :\n"))
coefficients_of_a =float(input("Enter the coefficients of a :\n"))
coefficients_of_b =float(input("Enter the coefficients of b :\n"))
coefficients_of_c =float(input("Enter the coefficients of c :\n"))

Quadratic = coefficients_of_a * (number**2) * (coefficients_of_b * number) + coefficients_of_c
print("Quadratic equation is ",Quadratic)