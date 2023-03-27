from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import scan_loader


online_loader = []
scan_loader.check_online_loaders() #fungsi scanning loader return hasil yang online
options = webdriver.ChromeOptions()
options.headless = False

print(scan_loader.online_loader)

for i in scan_loader.online_loader:
with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options) as browser:
	#browser = webdriver.Chrome()
		browser.get('http://' + str(i))
			try:
				WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, 'login')))
				search=browser.find_element(By.VALUE, 'Log In')
				search.click()
				print('okemantap')
			except TimeoutException:
				print('gagal')

