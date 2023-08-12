from selenium import webdriver
from selenium.webdriver.common.by import By
import time
log_in =webdriver.Chrome() #openning chrome
time.sleep(5)#delay because while oppenning chrome takes some secs to open
log_in.get("https://accounts.zoho.in/signin?servicename=zohopeople&signupurl=https://www.zoho.in/people/signup.html")
log_in.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[3]/div[2]/form[1]/div[2]/div[1]/div/span/input").send_keys("balkumarv@univisiontechnocon.com")
log_in.find_element(By.XPATH,"/html/body/div[5]/div[1]/div[3]/div[2]/form[1]/button").click()
time.sleep(60) #delay 60 secs for OTP
log_in.find_element(By.XPATH,"//*[@id='nextbtn']/span").click()  #clicking the verify button


