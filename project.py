# 1st project
# print('Hello Python World')
#########################
#2nd project
# import json
#
# if __name__ == '__main__':
#     try:
#         with open('input.json', 'r') as f:
#             data = json.loads(f.read())
#
#         output = ','.join([*data[0]])
#         for obj in data:
#             output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'
#
#         with open('output.csv', 'w') as f:
#             f.write(output)
#     except Exception as ex:
#         print(f'Error: {str(ex)}')

####################################################################
# import random
# import string
#
# total = string.ascii_letters + string.digits + string.punctuation
#
# length = 16
#
# password = "".join(random.sample(total, length))
#
# print(password)

#Another method
# import random
# import math
#
# alpha = "abcdefghijklmnopqrstuvwxyz"
# num = "0123456789"
# special = "@#$%&*"
#
# # pass_len=random.randint(8,13)  #without User INput
# pass_len = int(input("Enter Password Length"))
#
# # length of password by 50-30-20 formula
# alpha_len = pass_len//2
# num_len = math.ceil(pass_len*30/100)
# special_len = pass_len-(alpha_len+num_len)
#
#
# password = []
#
#
# def generate_pass(length, array, is_alpha=False):
#     for i in range(length):
#         index = random.randint(0, len(array) - 1)
#         character = array[index]
#         if is_alpha:
#             case = random.randint(0, 1)
#             if case == 1:
#                 character = character.upper()
#         password.append(character)
#
#
# # alpha password
# generate_pass(alpha_len, alpha, True)
# # numeric password
# generate_pass(num_len, num)
# # special Character password
# generate_pass(special_len, special)
# # suffle the generated password list
# random.shuffle(password)
# # convert List To string
# gen_password = ""
# for i in password:
#     gen_password = gen_password + str(i)
# print(gen_password)

################################################################

# import os
#
# text = input("input text : ")
#
# path = input("path : ")
#
# # os.chdir(path)
#
#
# def getfiles(path):
#     f = 0
#     os.chdir(path)
#     files = os.listdir()
#     # print(files)
#     for file_name in files:
#         abs_path = os.path.abspath(file_name)
#         if os.path.isdir(abs_path):
#             getfiles(abs_path)
#         if os.path.isfile(abs_path):
#             f = open(file_name, "r")
#             if text in f.read():
#                 f = 1
#                 print(text + " found in ")
#                 final_path = os.path.abspath(file_name)
#                 print(final_path)
#                 return True
#
#     if f == 1:
#         print(text + " not found! ")
#         return False
#
#
# getfiles(path)

################################################
# import requests as rq
# from bs4 import BeautifulSoup
#
# url = input("Enter Link: ")
# if ("https" or "http") in url:
#     data = rq.get(url)
# else:
#     data = rq.get("https://" + url)
# soup = BeautifulSoup(data.text, "html.parser")
# links = []
# for link in soup.find_all("a"):
#     links.append(link.get("href"))
#
# # Writing the output to a file (myLinks.txt) instead of to stdout
# # You can change 'a' to 'w' to overwrite the file each time
# with open("myLinks.txt", 'a') as saved:
#     print(links[:10], file=saved)

###############################################
import os
from PIL import Image

def watermark_photo(input_image_path,watermark_image_path,output_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path).convert("RGBA")
    # add watermark to your image
    position = base_image.size
    newsize = (int(position[0]*8/100),int(position[0]*8/100))
    # print(position)
    watermark = watermark.resize(newsize)
    # print(newsize)
    # return watermark

    new_position = position[0]-newsize[0]-20,position[1]-newsize[1]-20
    # create a new transparent image
    transparent = Image.new(mode='RGBA',size=position,color=(0,0,0,0))
    # paste the original image
    transparent.paste(base_image,(0,0))
    # paste the watermark image
    transparent.paste(watermark,new_position,watermark)
    image_mode = base_image.mode
    print(image_mode)
    if image_mode == 'RGB':
        transparent = transparent.convert(image_mode)
    else:
        transparent = transparent.convert('P')
    transparent.save(output_image_path,optimize=True,quality=100)
    print("Saving"+output_image_path+"...")

folder = input("Enter Folder Path:")
watermark = input("Enter Watermark Path:")
os.chdir(folder)
files = os.listdir(os.getcwd())
print(files)

if not os.path.isdir("output"):
    os.mkdir("output")

c = 1
for f in files:
    if os.path.isfile(os.path.abspath(f)):
        if f.endswith(".png") or f.endswith(".jpg"):
            watermark_photo(f,watermark,"output/"+f)