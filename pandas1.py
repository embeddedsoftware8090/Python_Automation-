import pandas as pd

# p11=pd.DataFrame({"Name":["shanan","deepu","sinchu"],"Salary":[8000,8500,9000]})
# print(p11)

#--------------------------------------------------------------
# df=pd.read_csv("C:/Users/Balkumar/desktop/submission.csv")
# print(df.head())#first 5 records
# print(df.tail())
# print(df.describe()) #

#-----------------------------------------------------
# import matplotlib.pyplot as plt
# x=[1001,1002,1003,1004,1005,1006] #
# #x =["Bal","Kumar","vishwa","Pushpa","Depu","univision"]
# y=[10000,23000,50000,18000,16500,12000]
# #y = ["F","B","C","D","E","A"]
# plt.bar(x,y,label="sales Department",color="pink")
# plt.xlabel('Empid')
# plt.ylabel('salaries')
# plt.legend()
# print(plt.show())

#----------------------------------------------------------

import matplotlib.pyplot as plt
slices=[50,20,15,15]
departments=["finance","prodction","HR","sales"]
cols=['pink','red','green','yellow']
plt.pie(slices,labels=departments,colors=cols,startangle=90,explode=(0,0.2,0,0),shadow=True,autopct='%0.1f')
plt.title('Univision Technology ')
plt.legend()
plt.show()

