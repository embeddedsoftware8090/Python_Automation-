#How Can You Check Whether a Pandas Dataframe Is Empty or Not?

# import pandas as pd
# df=pd.DataFrame({A:[]})
# print(df.empty)

#------------------------------------------------
#Write a Code to Sort an Array in Numpy by the (N-1)Th Column.
# import numpy as np
# X=np.array([[1,2,3],[0,5,2],[2,3,4]])
# print(X[X[:,1].argsort()])

#_---------------------------------------------------------
#Write a Python program to determine whether a number is binary.

num = 1101001
while(num > 0):
    l = num % 10
    if l!=0 and l!=1:
        print("given number is not binary")
    break
num = num // 10
if num == 0:
    print("given n umber is binary")

