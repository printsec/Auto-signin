from termcolor import colored
import pyfiglet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os


start = input('[*] Do you want to start? y/n: ')


if start == "y":
     print("Here we go :)")

else:
     print("Oh ok..")
     sys.exit()

os.system('clear')


Done = pyfiglet.figlet_format("Done")
banner = pyfiglet.figlet_format("Auto Sign-in")

def asciiBanner():
    print(colored(banner, 'green'))
    print(colored("Creator: ", 'blue') + "printsec")
    print("\n\n")
asciiBanner()



usernameStr = input("[*] Gmail: ")
passwordStr = input("[*] Password: ")
os.system('clear')

print(colored("signing in...", "blue"))

browser = webdriver.Firefox()
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))



username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()



password = WebDriverWait(browser, 10).until(
     EC.presence_of_element_located((By.NAME, 'password')))
     
password.send_keys(passwordStr)

signInButon = browser.find_element_by_id('passwordNext')
signInButon.click()


os.system('clear')
print(colored(Done, "blue"))





