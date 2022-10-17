try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Not a valid number")
except ZeroDivisionError:
    print("Age cannot be 0")

# furniture = ['table', 'chair', 'rack', 'shelf']
# for index, item in enumerate(furniture):
#     pass
#
#     print(f'index: {index} - item: {item}')

# l1 = [1,2,3,4,5,6,7,8,9]
# index = 0
# while index<=len(l1):
#     if index ==5:
#         continue
#     print(index)
#     index +=1




# l1 = ['B','a','l','k','u','m','a','r' ,'V','i','s','h','w','a','k','a','r','m','a']
# for str1 in l1:
#     print(str1)
#     print()
#     #print(str1[::-1])

# list1 = [1,2,3,4,5,6,7,8,9]
# new_list =len(list1)
# num = 0
# while num >=new_list - 1:
#     print(num)
#     num -= 1

# list1 = [1,2,3,4,5,6,7,8,9]
# #list1.reverse()
# new = reversed(list1)
# #for number in list1:
# print(new)

# list1 = [1,2,3,4,5,6,7,8,9]
# new_list = []
# for number in list1:
#     new_list = [number] + new_list
#     print(number)
#     print(new_list)
###########################################################
# original_list = [1, 2, 3, 4, 5]
# print("List before reverse : ",original_list)
# reversed_list = []
# for value in original_list:
#   reversed_list.insert(0,value)
# print("List after reverse : ", reversed_list )

