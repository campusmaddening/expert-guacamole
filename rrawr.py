import undetected_chromedriver as uc
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import json
import os
import requests
from selenium.webdriver.common.by import By

options = uc.ChromeOptions()
a = True
low_word = "abcdefghijklkmnopqrstuvwxyz"
upper_word = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%&*"
username_for = low_word
password_for = low_word + upper_word + number + symbols
long_password = 16
long_username = 12
options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
#options.user_data_dir = "rawr"
options.add_argument("--window-size=1920,1080")
#options.add_argument('--user-data-dir=rawr')
options.add_argument("--remote-debugging-port=38223")
driver = uc.Chrome(options=options, version_main=103)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1920, 1080)
time.sleep(random.randint(15, 200))
headers = {
'cache-control': "no-cache"
}
response = requests.request("GET", "https://zeksyntrantrebind.github.io/bookish-fiesta/a.txt", headers=headers)
driver.get(response.text.strip())
rawr = time.time()+60
while a == True:
  time.sleep(0.1)
  driver.switch_to.window(driver.window_handles[0])
  if(time.time()>rawr):
    rawr = time.time()+60
    headers = {
    'cache-control': "no-cache"
    }
    response = requests.request("GET", "https://zeksyntrantrebind.github.io/bookish-fiesta/38.txt", headers=headers)
    if(response.text.strip()=="meow"):
        a = False
