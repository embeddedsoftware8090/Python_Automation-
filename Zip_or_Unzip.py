'''zipfile.ZIP_STORED: No compression (default)
zipfile.ZIP_DEFLATED: Usual ZIP compression
zipfile.ZIP_BZIP2: BZIP2 compression
zipfile.ZIP_LZMA: LZMA compression  '''
import zipfile
with zipfile.ZipFile("C:/Users/Balkumar/Documents/balkumar.zip","w",compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write("C:/Users/Balkumar/Documents/file.txt")
    my_zip.write("C:/Users/Balkumar/Documents/image.png")


#creating zip file-------------------------------------------------
import zipfile
with zipfile.ZipFile("C:/Users/Balkumar/Documents/balkumar.zip","w") as my_zip:
    my_zip.write("C:/Users/Balkumar/Documents/file.txt")
    my_zip.write("C:/Users/Balkumar/Documents/image.png")




#-----------------------------------------------------------------
# import zipfile
# zip_file = zipfile.ZipFile("C:/Users/Balkumar/Documents/balkumar.zip","w")
# zip_file.write("C:/Users/Balkumar/Documents/file.txt")
# zip_file.write("C:/Users/Balkumar/Documents/image.png")
# zip_file.close()


# existinng file location zip file creation---------------------------------

# import zipfile
# zip_file = zipfile.ZipFile('C:/Users/Balkumar/Documents/file.zip','w')
# zip_file.write('file.txt', compress_type=zipfile.ZIP_DEFLATED)
# zip_file.close()

#zip creation in directory---------------------------------------------------

# import zipfile
# zip_file = zipfile.ZipFile('temp.zip','w')
# zip_file.write('temp.txt', compress_type=zipfile.ZIP_DEFLATED)
# zip_file.close()

#-----------------------------------------------------------------------------------
# # Python code to demonstrate the working of
# # unzip
#
# # initializing lists
# name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
# roll_no = [4, 1, 3, 2]
# marks = [40, 50, 60, 70]
#
# # using zip() to map values
# mapped = zip(name, roll_no, marks)
#
# # converting values to print as list
# mapped = list(mapped)
#
# # printing resultant values
# print("The zipped result is : ", end="")
# print(mapped)
#
# print("\n")
#
# # unzipping values
# namz, roll_noz, marksz = zip(*mapped)
#
# print("The unzipped result: \n", end="")
#
# # printing initial lists
# print("The name list is : ", end="")
# print(namz)
#
# print("The roll_no list is : ", end="")
# print(roll_noz)
#
# print("The marks list is : ", end="")
# print(marksz)


#--------------------------------------------------------------------
# names = ['Mukesh', 'Roni', 'Chari']
# ages = [24, 50, 18]
#
# for i, (name, age) in enumerate(zip(names, ages)):
# 	print(name, age)

#-------------------------------------------------------------------------------
# name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
# roll_no = [ 4, 1, 3, 2 ]
#
# # using zip() to map values
# mapped = zip(name, roll_no)
#
# print(set(mapped))
#----------------------------------------------------------------------------


# import re
# U=open("content.txt","r")
# read=U.read()
# res = re.findall(r"[A-Za-z0-9._%+-]+"
#                                         r"@[A-Za-z0-9.-]+"
#                                         r"\.[A-Za-z]{2,4}"
#                                     r"\-[\d]{10}", read)
# print(res)
#
