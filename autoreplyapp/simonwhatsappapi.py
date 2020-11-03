import time

from selenium import webdriver

from simon.accounts.pages import LoginPage
from simon.chat.pages import ChatPage
from simon.chats.pages import PanePage
from simon.header.pages import HeaderPage
from selenium.webdriver.common.alert import Alert
from django.shortcuts import render
from django.http import HttpResponse
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
# Creating the driver (browser)
# driver = webdriver.Firefox('/Users/yudiz/Downloads/')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://web.whatsapp.com')
driver.maximize_window()

# Login
#       and uncheck the remember check box
#       (Get your phone ready to read the QR code)
login_page = LoginPage(driver)
login_page.load()
time.sleep(7)


# 1. Get all opened chats
#       opened chats are the one chats or conversations
#       you already have in your whatsapp.
#       IT WONT work if you are looking for a contact
#       you have never started a conversation.
pane_page = PanePage(driver)

# get all chats
opened_chats = pane_page.opened_chats
k = 0
# iterating over them
for oc in opened_chats:
    k +=1
    print(k)
    print(oc.name)  # contact name (as appears on your whatsapp)
 

# 2. Go into the chat
#       just click on one to open the chat page
#       (where the conversation is happening)


# Logout


# Close the browser
driver.quit()