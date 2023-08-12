
#-----------------------------------------------------------
# def function1(name,age):
#     print(name,age) #print value
# function1("Balkumar",24) #call the value


#-------------------------------------------------------------
#Create a function with variable length of arguments

# def func1(*nums):
#    for i in nums:
#        print(i)
# print("func1:")
# func1(10)
# print("func1:")
# func1(10,20)
# print("func1:")
# func1(10,20,30)
# print("func1:")
# func1(10,20,30,40)

#------------------------------------------------------------------
#Return multiple values from a function
# def calculation(a, b):
#     sub =a-b
#     sum1 =a+b
#     return sub,sum1
# res = calculation(40, 100)
# print(res)

# def calculation(a, b):
#     return a*b,a/b
# add, sub = calculation(40, 10)
# print(add, sub)

#------------------------------------------------
from selenium import webdriver
import requests as rq
import os
from bs4 import BeautifulSoup
import time

# path= E:\web scraping\chromedriver_win32\chromedriver.exe
path = input("Enter Path : ")

url = input("Enter URL : ")

output = "output"


def get_url(path, url):
    driver = webdriver.Chrome(executable_path=r"{}".format(path))
    driver.get(url)
    print("loading.....")
    res = driver.execute_script("return document.documentElement.outerHTML")

    return res


def get_img_links(res):
    soup = BeautifulSoup(res, "lxml")
    imglinks = soup.find_all("img", src=True)
    return imglinks


def download_img(img_link, index):
    try:
        extensions = [".jpeg", ".jpg", ".png", ".gif"]
        extension = ".jpg"
        for exe in extensions:
            if img_link.find(exe) > 0:
                extension = exe
                break

        img_data = rq.get(img_link).content
        with open(output + "\\" + str(index + 1) + extension, "wb+") as f:
            f.write(img_data)

        f.close()
    except Exception:
        pass


result = get_url(path, url)
time.sleep(60)
img_links = get_img_links(result)
if not os.path.isdir(output):
    os.mkdir(output)

for index, img_link in enumerate(img_links):
    img_link = img_link["src"]
    print("Downloading...")
    if img_link:
        download_img(img_link, index)
print("Download Complete!!")