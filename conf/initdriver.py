from selenium.webdriver import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
action = ActionChains(driver)