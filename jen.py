from selenium import webdriver
import time


textbox_username_id="j_username"
textbox_password_id="j_password"
button_submit_name="Submit"

baseURL="http://localhost:8080/"
username='admin'
password='admin'

driver=webdriver.Chrome(executable_path="/usr/bin/chromedriver")
# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get(baseURL)
driver.find_element_by_id(textbox_username_id).send_keys(username)
driver.find_element_by_name(textbox_password_id).send_keys(password)
driver.find_element_by_name(button_submit_name).click()
driver.implicitly_wait(10)
time.sleep(10)
# driver.implicitly_wait(1000000000000)
driver.close()
driver.quit()
