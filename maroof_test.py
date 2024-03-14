import time
from csv import writer
from datetime import datetime
from urllib.parse import unquote

from selenium import webdriver
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


"""
اسم
رقم تليفون
عنوان
ولوكيشن
والمنهج التعليمي
عدد فصول
الريت
ترتيبهم ف المملكة أبتدائي وإعدادي وثانوي ولا واحد من التلاته 
لو في صور
"""

def main():
    service = Service()

    # instance of Options class allows us to configure Chrome
    options = webdriver.ChromeOptions()

    # options.add_argument('--headless')  # Uncomment to run without UI (Headless)

    # initializing webdriver for Chrome with our options
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://maroof.sa/businesses"  

    print("Opening Browser!")
    
    # Opening Main Page
    driver.get(url)


    # Wait 5 sec
    print("Waiting 5 Sec for Loader to Finsih!")
    time.sleep(5)
    
    cards = driver.find_elements(By.CSS_SELECTOR, ".storeCard")

    for card in cards:
        print(card.text)

    print("*" * 20)
    print("Finished Scrapping!")
    print("*" * 20)

    # close Browser
    driver.quit()


main()
