from selenium import webdriver
from selenium.webdriver.common.by import By
import time

fb =webdriver.Chrome()
fb.maximize_window()
fb.get("https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjY2NzEwODI3LCJjYWxsc2l0ZV9pZCI6MjY5NTQ4NDUzMDcyMDk1MX0%3D")
fb.find_element(By.NAME,"email").send_keys("8948163276")
fb.find_element(By.NAME,"pass").send_keys("708090")
fb.find_element(By.NAME,"login").click()
time.sleep(5)
fb.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div").click()
time.sleep(5)
fb.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/p").send_keys("Somewhere, something incredible is waiting to be known.")
# fb.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]").send_keys("Somewhere, something incredible is waiting to be known.")
# time.sleep(2)

# fb.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div").click()
# time.sleep(5)
# fb.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div/span/img").click()
# #
#
# fb.find_element(By.XPATH,"//*[@id='mount_0_0_Y9']/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]").click()

