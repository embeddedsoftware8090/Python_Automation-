import re
o=open("content.txt","r+")#open file in read or wtire mode
read=o.read()
res = re.findall(r"[A-Za-z0-9._%+-]+" ,read) #find all the data from file
print(res)


