from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():

    url = "http://www.naver.com"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    time.sleep(5)
    driver.quit()
