from selenium import webdriver

driver1 = webdriver.Chrome("C:\\Users\\Administrator\\Desktop\\chromedriver.exe")
driver1.get("https://www.aredray.xyz/ucp.php?mode=register")
agreeButton = driver1.find_element_by_id('agreed')

agreeButton.click()

userInput = driver1.find_element_by_id('username')
emailInput = driver1.find_element_by_id('email')
passInput = driver1.find_element_by_id('new_password')
passConfirmInput = driver1.find_element_by_id('password_confirm')
answerInput = driver1.find_element_by_id('answer')
sumbitButton = driver1.find_element_by_id('submit')
userInput.send_keys('DeepFuckingValue')
emailInput.send_keys('emaiL@domain.org')
passInput.send_keys('password123')
passConfirmInput.send_keys('password123')
answerInput.send_keys("Aredray")
sumbitButton.click()
