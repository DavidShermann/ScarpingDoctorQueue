

import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from tkinter import *


# def submit():
#     keyW = var.get()
#     root.destroy()


# root = Tk()

# var = StringVar()
# # specify size of window.
# root.geometry("350x100")

# root.eval('tk::PlaceWindow . center')

# # Create text widget and specify size
# t = Entry(root,font = ("Ariel",14),textvariable=var)

# # Create label
# l = Label(root, text = "Insert keyword for finding a doctor")
# l.config(font =("Ariel", 14))
# l.pack()
# t.pack() 

# # Create an Exit button.
# b2 = Button(root, text = "OK",command=submit,font =("Ariel", 14))
# b2.pack()


# root.mainloop()

#keyWord = var.get()

def scrapeDoctor():






    return
keyW = 'עיניים'
print(keyW)
options = Options()
#options.headless = True
options.add_argument("--window-size=1920,1200")

#DRIVER_PATH = 'C:\\Users\\Sherman\\Downloads\\test_folder\\chromedriver'
DRIVER_PATH = 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\projects\\helloworld\\chromedriver'

driver = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)


#opening a browser
driver.get('https://online.maccabi4u.co.il/')

#Login to an account
click1 = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[1]/a').click()
login = driver.find_element(By.XPATH,'//*[@id="identifyWithPasswordCitizenId"]').send_keys('208733360')
passW = driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('HGTarMH3UKgeR8b')
click2 = driver.find_element(By.XPATH,'//*[@id="IdentifyWithPassword"]/button').click()
time.sleep(10)

clickDialog = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/button').click()


#moving to search a doctor sector by keywords
click3 = driver.find_element(By.XPATH,'//*[@id="app-wrap"]/div/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/div/div/div[5]/div/button').click()
time.sleep(3)
click4 = driver.find_element(By.XPATH,'//*[@id="app-wrap"]/div/div[3]/div/div[1]/div[2]/div[2]/div[2]/a[2]/button').click()
click5 = driver.find_element(By.XPATH,'//*[@id="app-wrap"]/div/div[3]/div/div[1]/div[2]/div[2]/div[3]/div/button[1]').click()
time.sleep(3)



#scraping all doctors,available hours in dates and doctors' professions

click6 = driver.find_element(By.XPATH,'//*[@aria-selected="false"]').click()
time.sleep(1)
click7 = driver.find_element(By.NAME,'search').send_keys(keyW)
time.sleep(1)
#click8 = driver.find_element(By.XPATH,'//*[@id="asasas0"]').click()
try:
    driver.find_element(By.XPATH,'//*[@id="SearchBtn"]').click()
except:
    driver.find_element(By.XPATH,'//*[@id="searchInput_pop"]/button/span').click()    
time.sleep(5)



list = re.findall("[0-9]+", driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div[3]/div[3]/div[2]/nav/div').text)
pages = max(list)
#print(pages)
pages = int(pages)
for page in range(1,pages + 1):
    doctors = driver.find_elements(By.XPATH,'//*[@id="app"]/div/div/div/div/div[3]/div[3]/div[2]/div[2]/div')
    for doctor in doctors:
        for i in range(10):#need to find how to limit the range according to the count of names in a page
            #scrape for free hours for appointment
            doctor_name = doctor.find_element(By.XPATH,'//*[@id="index{}"]'.format(i)).text
            first_available_date = doctor.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[4]/div/div[2]').text
            print(doctor_name+" "+first_available_date)
            doctor.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[4]/a').click()
            time.sleep(10)


            click_type_appoint = driver.find_element(By.XPATH,'//*[@id="app-wrap"]/div/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/button').click()
         #  switch()
            dates = driver.find_elements(By.XPATH,'//*[@id="app-wrap"]/div/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[3]/div/div[1]/div[1]/div/div/div[2]/div/div[3]')
            for date in dates:
                openAppoint = date.find_element(By.CLASS_NAME,'DayPicker-Day DayPicker-Day--available')
                ##
                if(openAppoint):
                    openAppoint.click()
                    time.sleep(2.5)
                    AreaOfTime = driver.find_elements(By.XPATH,'//*[@id="app-wrap"]/div/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]')
                    for Area in AreaOfTime:
                        hours = driver.find_elements(By.ID,'//*[@id="btnsConatiner"]')
                        for hour in hours:
                            print (hour.find_element(By.CLASS_NAME,'RoundButtonPicker-module__button___CpANh Button-module__btn___LwGuZ btn btn-outline-secondary').text)
                driver.find_element(By.XPATH,'//*[@id="app-wrap"]/div/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[3]/div/div[1]/div[1]/div/div/div[1]/span[2]').click()
                time.sleep(2.5)        


    if page == pages:
        break
    driver.find_element(By.LINK_TEXT,'{}'.format(page + 1)).click()
    time.sleep(1)        


#driver.close()

