from selenium import webdriver
from time import sleep
import random
from pyfiglet import Figlet
from termcolor import colored
from colorama import Fore, Back, Style
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('SomalPY'))
print("By 0k3y ")
print (" ")

print(Fore.RED + 'some red text') 

size = 1


print("Browser = OFF")
print(" COMMANDS ")
print("start = start the script")
print("on = the browser will be displayed")
print("off = the browser will run in background")
print("tags = to define keywords (the result will be displayed here")
print(" ")

tags = 0

tagstr = ("null")

while True:
    cmd = input("Type: ")
    if cmd == "on":
        size = 1
        print ("Setting changed to on")
    if cmd == "off":
        size = 2
        print ("Setting changed to off")
    if cmd == "tags":
        print ("Please type your tags. Seperate them with an , ")
        tagsraw = input("Type: ")
        tags = [tagsraw]
        tagstr = str(tags)
        print (tagstr + " have been added to tags")
    if cmd == "start":
        print ("Started successfully")
        driver = webdriver.Firefox()
        if size == 1:
            driver.maximize_window()
        if size == 2:
            driver.minimize_window()
        driver.get("https://translate.google.com/?hl=de#view=home&op=translate&sl=so&tl=de&text=")
        sleep(7)
        while True:
            n = random.randint(1,4)
            a = str(n)
            ##x = 1
            for i in range(n):
                driver.find_element_by_xpath(
                '//*[@id="source"]').send_keys("ke")
                sleep(1)
                output = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/span").text
                inpute = driver.find_element_by_xpath('//*[@id="source"]').text
                print (output)
                if any(x in output for x in tagstr):
                    print ("TAG FOUND!")
                    print (output)
                    print (inpute)
                    
                elif "kekeke ke" in output:
                    driver.get("https://translate.google.com/?hl=de#view=home&op=translate&sl=so&tl=de&text=")
                elif "...." in output:
                    driver.get("https://translate.google.com/?hl=de#view=home&op=translate&sl=so&tl=de&text=")
            driver.find_element_by_xpath(
                '//*[@id="source"]').send_keys(" ")
