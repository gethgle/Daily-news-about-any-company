from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.chrome.options import Options

url = 'https://www.tickertape.in/stocks/indian-railway-finance-corporation-IRF/news?checklist=basic&type=news'
drive_path = r"C:\Users\shankar\Desktop\projects\chromedriver.exe"

options = Options()
options.headless =False
driver= webdriver.Chrome(executable_path=drive_path,options=options)

driver.get(url)
# keep clicking untill no click buttion
while True:
	time.sleep(1.5)
	try:
		load_more = driver.find_element_by_name("Load more")
		load_more.click()
	except NoSuchElementException:
		break

urls = driver.find_elements_by_xpath("//div[@data-section-tag='latestNews' or @data-section-tag='olderNews']/div/a/")

driver.find_element_by_class_name()

driver.find_element_by_tag_name()

print(len(urls))



