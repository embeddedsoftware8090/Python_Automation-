'''r for reading – The file pointer is placed at the beginning of the file. This is the default mode.
r+ Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
w Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
w+ Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.'''

#using r -----------------------------------------------------------
# import re
# # a=open("C:/Users/Balkumar/Documents/file.txt","r")
# a=open("content.txt")
# read=a.read()
# res = re.findall(r"[A-Za-z0-9._%+-]+" ,read) #read data from file
# print(res)

#using w ----------------------------------------------
# import re
# a=open("content.txt","w")#wrting data in file
# read=a.write("univision Technology consulting pvt ltd")

# print(read)

#using r+-----------------------------------------------------

# import re
# files = open("content.txt","r+") #reading and wrting from end of lines
# res = files.read()
# #res = files.write("Vishwakarma")
# print(res)

#using w+-------------------------------------------------------
# import re
# files = open("content.txt","w+") #reading and wrting new file and overwrite the existing or not
# res = files.read()
# #res = files.write("location")
# print(res)

#ab--------------------------------------

