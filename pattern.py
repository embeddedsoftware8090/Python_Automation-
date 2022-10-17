# row =int(input("Enter the number of rows:\n"))
# for i in range(row):
#     for j in range(row):
#         if i==0:
#             print("a  ",end="")
#         elif j==0:
#             print("b  ", end="")
#         elif i==(row-1):
#             print("c  ",end="")
#         elif j==(row-i):
#             print("d  ", end="")
#     print("")
# Python 3 code for hollow rectangle


# Function to print hollow rectangle
#n =int(input("Enter the n numbers:\n"))
#m =int(input("Enter the m numbers:\n"))

def print_rectangle(n, m):
    for i in range(n+1):
        for j in range(m+1):
            if ((i == 0 or i == n ) or
                    (j == 0 or j == m)):
                print("* ", end=" ")
            else:
                print(" ", end="  ")

        print()


# Driver program for above function
rows = 6
columns = 6
print_rectangle(rows, columns)

# This code is contributed by Nikita Tiwari.
