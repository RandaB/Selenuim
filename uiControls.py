from selenium import webdriver

#browser exposes an executable file
#through selenuim test we need to invoke the executable file which will then invoke actual
driver = webdriver.Chrome(executable_path="C:\\Users\\s\\Documents\\driver\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
