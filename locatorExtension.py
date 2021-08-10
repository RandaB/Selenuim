from selenium import webdriver
#browser exposes an executable file
#through selenuim test we need to invoke the executable file which will then invoke actual
driver = webdriver.Chrome(executable_path="C:\\Users\\s\\Documents\\driver\\chromedriver.exe")

driver.get("https://login.salesforce.com/")

driver.find_element_by_css_selector("#username").send_keys("Randa")
driver.find_element_by_css_selector(".password").send_keys("Randa")
driver.find_element_by_link_text("Mot de passe oublié ?").click()

driver.find_element_by_xpath("//input[@name = 'cancel']").click()

print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
