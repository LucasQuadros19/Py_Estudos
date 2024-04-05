from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By 
from selenium.webdriver.safari.options  import Options
import os
from time import sleep

os.system('clear')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('window-size=400,800')
# options.add_argument('--headless')
navegador = webdriver.Chrome(options=options)

navegador.get('https://www.airbnb.com.br')
sleep(2)
site= BeautifulSoup(navegador.page_source, 'html.parser')

elemento_input = driver.find_element_by_id('bigsearch-query-location-input')
elemento_input.send_keys('nurburg')




