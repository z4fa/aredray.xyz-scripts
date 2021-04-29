from selenium import webdriver
import time

driver1 = webdriver.Chrome("C:\\Users\\Administrator\\Desktop\\chromedriver.exe")
driver2 = webdriver.Chrome("C:\\Users\\Administrator\\Desktop\\chromedriver.exe")
driver3 = webdriver.Chrome("C:\\Users\\Administrator\\Desktop\\chromedriver.exe")
driver4 = webdriver.Chrome("C:\\Users\\Administratorr\\Desktop\\chromedriver.exe")
driver5 = webdriver.Chrome("C:\\Users\\Administrator\\Desktop\\chromedriver.exe")
x = 0

url = "https://www.aredray.xyz/viewtopic.php?f=example&t=example"

while True:
    driver1.get(url)
    driver2.get(url)
    driver3.get(url)
    driver4.get(url)
    driver5.get(url)
    time.sleep(10)
    x += 1
    print(x)
