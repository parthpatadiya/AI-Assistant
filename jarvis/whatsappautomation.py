from selenium import webdriver
import selenium.webdriver.common.by as By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time

driver = webdriver.Chrome(executable_path="C:/Users/Microsoft/Desktop/chromedriver.exe")

def open_whatsapp():
    driver.get('https://web.whatsapp.com/')
    time.sleep(9)

def send_message(person_name,message):
    try:
        print(person_name)
        try :
            driver.find_element_by_xpath('//span[@title="{}"]'.format(person_name))
            person=WebDriverWait(driver,15).until(EC.visibility_of(driver.find_element_by_xpath('//span[@title="{}"]'.format(person_name))))
            person.click()
        except:
            driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input').send_keys(person_name)
            time.sleep(5)
            person=WebDriverWait(driver,15).until(EC.visibility_of(driver.find_element_by_xpath('//span[@title="{}"]'.format(person_name))))
            person.click()
    
        time.sleep(1.3)
        msgbox=WebDriverWait(driver,15).until(EC.visibility_of(driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))
        msgbox.send_keys(str(message))
    
        WebDriverWait(driver,15).until(EC.visibility_of(driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')))
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click();
        return True
    except:
        return False

#send_message("Karan","Su karas?")