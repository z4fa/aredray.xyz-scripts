from selenium import webdriver
import time

driver1 = webdriver.Chrome("C:\\Users\\Artur\\Desktop\\chromedriver.exe")
driver2 = webdriver.Chrome("C:\\Users\\Artur\\Desktop\\chromedriver.exe")
driver3 = webdriver.Chrome("C:\\Users\\Artur\\Desktop\\chromedriver.exe")
driver4 = webdriver.Chrome("C:\\Users\\Artur\\Desktop\\chromedriver.exe")
driver5 = webdriver.Chrome("C:\\Users\\Artur\\Desktop\\chromedriver.exe")
x = 0

while True:
    driver1.get("https://www.aredray.xyz/viewtopic.php?f=4&t=162")
    driver2.get("https://www.aredray.xyz/viewtopic.php?f=4&t=162")
    driver3.get("https://www.aredray.xyz/viewtopic.php?f=4&t=162")
    driver4.get("https://www.aredray.xyz/viewtopic.php?f=4&t=162")
    driver5.get("https://www.aredray.xyz/viewtopic.php?f=4&t=162")
    time.sleep(10)
    x += 1
    print(x)
