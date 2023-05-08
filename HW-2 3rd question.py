from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
driver.find_element(By.XPATH, "//span[text()='Returns']").click()
expected_result_1 = "Sign in"
actual_result_1 = driver.find_element(By.XPATH, "// h1 [ @ class = 'a-spacing-small']").text
driver.find_element(By.XPATH, "//input[@type='email']")
assert expected_result_1 == actual_result_1, f"expected {expected_result_1} but got {actual_result_1}"
print("Test passed")
driver.quit()