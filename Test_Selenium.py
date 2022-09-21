



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
#options.headless = True
options.add_argument("--window-size=1920,1200")


DRIVER_PATH = 'C:\\Users\\Sherman\\Downloads\\test_folder\\chromedriver'
#driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)


driver.get('https://online.maccabi4u.co.il/')
click1 = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[1]/a').click()
login = driver.find_element(By.XPATH,'//*[@id="identifyWithPasswordCitizenId"]').send_keys('208733360')
passW = driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('HGTarMH3UKgeR8b')
click2 = driver.find_element(By.XPATH,'//*[@id="IdentifyWithPassword"]/button').click()
time.sleep(7)
click3 = driver.find_element(By.XPATH,'//*[@id="app-wrap"]/div/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/div/div/div[5]/div/button').click()
time.sleep(5)
click4 = driver.find_element(By.XPATH,'//*[@id="app-wrap"]/div/div[3]/div/div[1]/div[2]/div[2]/div[2]/a[2]/button').click()
click5 = driver.find_element(By.XPATH,'//*[@id="app-wrap"]/div/div[3]/div/div[1]/div[2]/div[2]/div[3]/div/button[1]').click()






