from selenium import webdriver
from selenium.webdriver.support.ui import Select

#browser exposes an executable file
#through selenuim test we need to invoke the executable file which will then invoke actual
driver = webdriver.Chrome(executable_path="C:\\Users\\s\\Documents\\driver\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Randa")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_css_selector("input[name='name']").send_keys("Randa")
driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)


#select class provide  the methods to handle the options in drop down
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
