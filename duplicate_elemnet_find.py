# # this input list contains duplicates
# mylist = [5, 3, 5, 2, 1, 6, 6, 4] # 5 & 6 are duplicate numbers.
#
# # find the length of the list
# print(len(mylist))
#
# # create a set from the list
# myset = set(mylist)
#
# # find the length of the Python set variable myset
# print(len(myset))
#
# # compare the length and print if the list contains duplicates
# if len(mylist) != len(myset):
#     print("duplicates found in the list")
# else:
#     print

####################################################################
# the given list contains duplicates
mylist = [5, 3, 5, 2, 2, 1, 1, 6, 6, 4] # the original list of integers with duplicates

newlist = [] # empty list to hold unique elements from the list
duplist = [] # empty list to hold the duplicate elements from the list
for i in mylist:
    if i not in newlist:
        newlist.append(i)
    else:
        duplist.append(i) # this method catches the first duplicate entries, and appends them to the list

# The next step is to print the duplicate entries, and the unique entries
print("List of duplicates", duplist)
print("Unique Item List", newlist) # prints the final list of unique items