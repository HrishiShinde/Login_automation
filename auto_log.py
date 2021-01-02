from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"  #Enter path of chromedriver here

def login(site, uname_name, uname, pwrd, text):
    driver = webdriver.Chrome(PATH)
    driver.get(site)
    time.sleep(3)

    username = driver.find_element_by_name(uname_name)
    username.click()
    username.send_keys(uname)

    password = driver.find_element_by_name("password")
    password.click()
    password.send_keys(pwrd)
    password.send_keys(Keys.RETURN)

    if text == 'i': 
        time.sleep(3)
        not_now1 = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
        not_now1.click()
        time.sleep(3)
        not_now2 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        not_now2.click()
    #submit_button = driver.find_element_by_name("commit")
    #submit_button.click()

while True:
    print("="*20)
    print("Where do you want to login?")
    print("Github ==> 'g'")
    print("Instagram ==> 'i'")
    print("Quit ==> 'q'")
    text = input("Press the corresponding key to login: ")
    print("="*20)

    if text == 'g':
        site = "https://github.com/login"
        name = "login"    
        email = "your_email"  #enter your email id of this site here
        pwd = "your_password"  #enter your password of this site here
        login(site, name, email, pwd, text)

    if text == 'i':
        site = "https://www.instagram.com/accounts/login/"
        name = "username"
        email = "your_email"  #enter your email id of this site here
        pwd = "your_password" #enter your password of this site here
        login(site, name, email, pwd, text)

    if text == 'q':
        print("Bye-bye!")
        break
#print(driver.title)
#driver.quit()
