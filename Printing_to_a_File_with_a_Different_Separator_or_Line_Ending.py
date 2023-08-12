import re
o=open("content.txt","r+")#open file in read or wtire mode
read=o.read()
res = re.findall(r"[A-Za-z0-9._%+-]+" ,read) #find all the data from file
print(res)
#------------------------------------------------------------------------
#mobile number validating
# import re
# #check = re.fullmatch('\d{3}([-]*)\d{6}',"080-265955")
# check = re.fullmatch(r"[+]\d{4}[-]\d{8}","+9188-38933994")
# print(check)
# if check:
#    print("Valid")
# else:
#    print("Invalid")


#---------------------------------------------------------

