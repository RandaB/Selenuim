from selenium import webdriver

#browser exposes an executable file
#through selenuim test we need to invoke the executable file which will then invoke actual
driver = webdriver.Chrome(executable_path="C:\\Users\\s\\Documents\\driver\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()


radiobuttons = driver.find_elements_by_name('radioButton')
radiobuttons[2].click()
assert radiobuttons[2].is_selected()