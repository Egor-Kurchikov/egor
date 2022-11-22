
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s=Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login") #Open website and login
driver.maximize_window() #Browser windows full screen
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click() #Selecting an authorization form
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("rimuru@yopmail.com") #Entering a login
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456") #Password entry
driver.find_element(By.CSS_SELECTOR, ".btn").click() #Clicking login button
time.sleep(7) #Waiting 7 seconds

driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click() #Open passport form
driver.find_element(By.ID, "surname").send_keys(Keys.CONTROL+"a") #Select text
driver.find_element(By.ID, "surname").send_keys(Keys.DELETE) #Clearing the input field
driver.find_element(By.ID, "surname").send_keys("Егоров") #Entering a last name
driver.find_element(By.ID, "name").send_keys(Keys.CONTROL+"a") #Select text
driver.find_element(By.ID, "name").send_keys(Keys.DELETE) #Clearing the input field
driver.find_element(By.ID, "name").send_keys("Гоша") #Entering a name
driver.find_element(By.ID, "patronymic").send_keys(Keys.CONTROL+"a") #Select text
driver.find_element(By.ID, "patronymic").send_keys(Keys.DELETE) #Clearing the input field
driver.find_element(By.ID, "patronymic").send_keys("Егорович") #Entering a patronymic
driver.find_element(By.NAME, "date").click() #Selecting a date of birth
time.sleep(5) #Waiting 5 seconds
driver.find_element(By.CSS_SELECTOR, ".mx-btn-current-year").click() #Click on the year
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > .cell:nth-child(1) > div").click() #Select year
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .cell:nth-child(1)").click() #Select month
driver.find_element(By.CSS_SELECTOR, ".mx-date-row:nth-child(3) > .cell:nth-child(1) > div").click() #Select day
driver.find_element(By.ID, "passportSeries").send_keys(Keys.CONTROL+"a") #Select text
driver.find_element(By.ID, "passportSeries").send_keys(Keys.DELETE) #Clearing the input field
driver.find_element(By.ID,  "passportSeries").send_keys(5555) #Entering a Passport Series
driver.find_element(By.ID, "passportNumber").send_keys(Keys.CONTROL+"a") #Select text
driver.find_element(By.ID, "passportNumber").send_keys(Keys.DELETE) #Clearing the input field
driver.find_element(By.ID, "passportNumber").send_keys(777777) #Entering the passport number
time.sleep(5) #Waiting 5 seconds
driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").click()  #Issue date selection
driver.find_element(By.CSS_SELECTOR, ".mx-btn-current-year").click()  #Click on the year
driver.find_element(By.CSS_SELECTOR, ".mx-icon-double-left").click()  #Double click left, select year
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > .cell:nth-child(2) > div").click()  #Select year
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > .cell:nth-child(3) > div").click()  #Select month
driver.find_element(By.CSS_SELECTOR, ".mx-date-row:nth-child(3) > .cell:nth-child(7) > div").click()  #Select day
driver.find_element(By.ID, "code").send_keys(Keys.CONTROL+"a") #Select text
driver.find_element(By.ID, "code").send_keys(Keys.DELETE) #Clearing the input field
driver.find_element(By.ID, "code").send_keys("888888")  #Entering department code
driver.find_element(By.ID, "cardId").send_keys(Keys.CONTROL+"a")  #Select text
driver.find_element(By.ID, "cardId").send_keys(Keys.DELETE) #Clearing the input field
driver.find_element(By.ID, "cardId").send_keys("09876543210")   #Entering the insurance number
driver.find_element(By.ID, "issued").send_keys(Keys.CONTROL+"a")  #Select text
driver.find_element(By.ID, "issued").send_keys(Keys.DELETE)  #Clearing the input field
driver.find_element(By.ID, "issued").send_keys("УФМС Челябинск") #Enter the field Date of issue
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.CONTROL+"a")  #Select text
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.DELETE)  #Clearing the input field
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("Челябинск")  #City entry
time.sleep(1) #Waiting 1 seconds
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.ARROW_DOWN)  #Selecting a city from the list
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.ENTER) #Selecting a city from the list
driver.find_element(By.ID, "phone").send_keys(Keys.CONTROL+"a")  #Select text
driver.find_element(By.ID, "phone").send_keys(Keys.DELETE)  #Clearing the input field
driver.find_element(By.ID, "phone").send_keys("9555555555")  #Entering a phone number
driver.find_element(By.ID, "privacy").click() #Uncheck the checkbox
time.sleep(2) #Waiting 2 seconds
driver.find_element(By.ID, "privacy").click() #Check box
time.sleep(3)  #Waiting 3 seconds
driver.execute_script('window.scrollTo(0,1500);') #Scroll down the screen
time.sleep(3)  #Waiting 3 seconds
filePath ='C:\\Users\\Hato\\PycharmProjects\\pythonProject\\img\\123.jpg'  #The path to the file
driver.find_element(By.CSS_SELECTOR, '#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div.form.passport-form.document-form > div.body > div.upload-widget.upload-widget > input[type=file]').send_keys(filePath) #Uploading a file to the site
time.sleep(4) #Waiting 4 seconds
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()  #Close the passport form
time.sleep(3)  #Waiting 3 seconds
driver.quit()  #Close website



































