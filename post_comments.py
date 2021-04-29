from selenium import webdriver

driver1 = webdriver.Chrome("C:\\Users\\Administrator\\Desktop\\chromedriver.exe")
driver1.get("https://www.aredray.xyz/ucp.php?mode=login&redirect=index.php&sid=6fc7a3622d92f59b871c22c2e2d66325") ## Login page

userInput = driver1.find_element_by_id('username') ## Finds credentials
passInput = driver1.find_element_by_id('password') ## Finds credentials
sumbitButton = driver1.find_element_by_name('login')

userInput.send_keys('user') ## Enters credentials
passInput.send_keys('password') ## Enters credentials
sumbitButton.click()

driver1.get("https://www.aredray.xyz/posting.php?mode=reply&f=example&t=example")

textboxInput = driver1.find_element_by_id('message') ## Finds Input
sumbitMessageButton = driver1.find_element_by_name('post') ## Finds Input
textboxInput.send_keys("Test") ### Message you want to post
sumbitMessageButton.click()
