#------ ------ ------ #AyazSaiyed  #November2020  #https://ayazsaiyed.ml ------ ------ ------#

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



def index(requests):
	return render(requests,'autoreplyapp/AutoResponMessages.html')

def autoreplying(requests):

	browser = webdriver.Chrome(ChromeDriverManager().install())

	browser.get('https://web.whatsapp.com/')
	print( " ----- ")
	print(" Opening the whatsapp web ")
	print( " ----- ")
	time.sleep(7)
	letsdoit(browser)
	return render(requests,'autoreplyapp/sendmessages.html')
	

def letsdoit(browser):

	# browser.execute_script("window.scrollTo(0,500);")
	try:
		titles = browser.find_elements_by_class_name("_3CneP")
		names_list = []
		names_list1 = []
		k = 0
		for info in titles:
			k = k+1
			names_list.append(info.text)
	except:
		pass

	# print(" Names ",names_list)
	
	for name in names_list:
	    try:
	        person = browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))

	        print("Person Name",name)
	        person.click()
	        # _357i8
	        
	        
	        #Get the list of messages exchanged with the person
	        message_list = browser.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
	        messages = []
	        for message in message_list:
	            messages.append(message.text)

	        #Checking the last message
	        if "happy" in messages[-1].lower() and "diwali" in messages[-1].lower():
	            print("Greeting found from "+name)
	            #Navigate to the type message here section
	            message_box = browser.find_element_by_xpath('//div[@class="_3uMse"]')
	            msg = "Thank you "+name+" ☺️ for wishes and a very Happiee diwalii to you too and your family"
	            time.sleep(0.2)
	            message_box.send_keys(msg)
	            message_button = browser.find_element_by_xpath('//button[@class="_1U1xa"]')
	            #Let's send
	            message_button.click()

	    except:
	        #Exceptions can occour if emojis present in names
	        continue
	# browser.close()

	return HttpResponse(" Messeages are Sent ")


