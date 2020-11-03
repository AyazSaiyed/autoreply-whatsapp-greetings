# /Users/yudiz/Downloads/MyExtraStuff/autoreplygreetings/autoreplyweb
# (base) Ayaz:autoreplyweb yudiz$ 

# https://dashboard.heroku.com/apps/autoreply-greetings/deploy/heroku-git

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
from selenium.webdriver.chrome.options import Options
# Create your views here.


GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

def index(requests):
	return render(requests,'autoreplyapp/AutoResponMessages.html')

def autoreplying(requests):
	print(" Function Called ")

	# browser = webdriver.Chrome(ChromeDriverManager().install())
	# browser = webdriver.Chrome('./chromedriver', chrome_options=Options) #Give the full path to chromedriver)
	browser = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
	browser.get('https://web.whatsapp.com/')
	time.sleep(7)
	letsdoit(browser)
	return HttpResponse(" Messeages Sent ")
	# return render(requests,'autoreplyapp/sendmessages.html')
	

def letsdoit(browser):
	# time.sleep(6)

	#Find the list of all names in the chat section
	# browser.execute_script("window.scrollTo(0,500);")
	try:
		titles = browser.find_elements_by_class_name("_3CneP")
		names_list = []
		names_list1 = []
		k = 0
		for info in titles:
			k = k+1
			# print("value ",k)
			names_list.append(info.text)
			# print("names",names_list)

	
	# 	# print(" In except")
	# 	initial = 800
	# 	for i in range(0, 2):
	# 		browser.execute_script("document.getElementById('pane-side').scrollTop={}".format(initial))
	# 		titles = browser.find_elements_by_class_name("_3CneP")
	# 		names_list = []
	# 		for info in titles:
	# 			names_list.append(info.text)
	# 			# print("names",names_list)
	# 	initial+=10
	except:
		pass

	print(" Names ",names_list)
	for name in names_list:
	    try:
	        #Open the chat of a specific person
	        person = browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))

	        print("Person Name",name)
	        person.click()
	        # _357i8
	        
	        # browser.execute_script("window.scrollTo(0,1);")
	        
	        #Get the list of messages exchanged with the person
	        message_list = browser.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
	        messages = []
	        for message in message_list:
	            messages.append(message.text)

	        #Checking the last message
	        if "happy" in messages[-1].lower() and "diwali" in messages[-1].lower():
	            print("Wish found")
	            #Navigate to the type message here section
	            message_box = browser.find_element_by_xpath('//div[@class="_3uMse"]')
	            msg = "Thank you "+name+" ☺️ for wishes and a very Happiee diwalii to you too and your family"
	            time.sleep(0.2)
	            #Typing message in that section
	            message_box.send_keys(msg)
	            #Accessing the send button
	            message_button = browser.find_element_by_xpath('//button[@class="_1U1xa"]')
	            #Clicking the send button
	            message_button.click()

	    except:
	        #Exceptions can occour if emojis present in names
	        continue
	# browser.close()

	return HttpResponse(" Messeages Sent ")


# autoreplya(requests)