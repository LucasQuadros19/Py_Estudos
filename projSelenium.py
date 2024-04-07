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
# 
navegador = webdriver.Chrome(options=options)

navegador.get('https://www.mercadolivre.com.br/')
sleep(2)
site= BeautifulSoup(navegador.page_source, 'html.parser')

elemento = navegador.find_element(By.TAG_NAME, 'input')
elemento.send_keys('guitarra')
elemento.submit()
sleep(0.5)
botao = navegador.find_element(By.LINK_TEXT, "Yamaha")
botao.click()









