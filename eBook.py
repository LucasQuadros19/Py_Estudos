from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By 
from selenium.webdriver.safari.options  import Options
import os
from time import sleep

options = webdriver.SafariOptions()
options.headless = True
driver = webdriver.Safari(options=options)

url_base = 'https://www.amazon.com/'
mainRoute = 's?i=stripbooks&rh=n%3A283155%2Cp_30%3AForgotten+Books%2Cp_n_feature_browse-bin%3A2656022011&s=exact-aware-popularity-rank&dc&language=pt&ds=v1%3AF62MM2U5pQxy5ihMMkiYz3DXl5SKe%2FaUTy9uSUSDxkc&Adv-Srch-Books-Submit.x=35&Adv-Srch-Books-Submit.y=4&qid=1712363856&unfiltered=1&ref=sr_st_exact-aware-popularity-rank'
driver.get(url_base + mainRoute)
sleep(2)
page_source = driver.page_source
site = BeautifulSoup(page_source, 'html.parser')

adverts = site.find('div', {'class': 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'})

link = driver.find_element(By.CSS_SELECTOR, "a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")





# Realizar o link GET do Selenium
driver.get(url_base + link['href'])
sleep(2)

# Obter a página do link
dataPage = driver.page_source
page = BeautifulSoup(dataPage, 'html.parser')
data = page.find('span', {'class':'a-size-extra-large celwidget'})

print(data.prettify())








"""
if adverts:
    print(adverts.prettify())
else:
    print("Nenhum anúncio encontrado.")

    



<a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/-/pt/dp/B0096161R0/ref=sr_1_1?Adv-Srch-Books-Submit.x=35&amp;Adv-Srch-Books-Submit.y=4&amp;dib=eyJ2IjoiMSJ9.cX1K9RE3Vzu58FDeOgZU5h9PQ3vbJSclZB1LEnhDJ6PSFTj1Ep6-P6M1OGu_eyvlMMyYrHveIpShZ4NuFvYADFwn8NXovYU5Qnh3YLRSe27vD48zejdqHfK61y4sFGjMcosUdPm16YQ9HBWryauuZinwCocPkG1Jebhi20x8E0K7_LFgrBIFxiTOteIjr6NKZH93BxVfTrgdZu8K-_LVivOC1zZEAizlMeJluea53rQ.C7y1x1CgNcBUzy6NEV9SH1LNK0CoOpSDAB2SYihe45c&amp;dib_tag=se&amp;qid=1712370796&amp;refinements=p_30%3AForgotten+Books%2Cp_n_feature_browse-bin%3A2656022011&amp;s=books&amp;sr=1-1&amp;unfiltered=1">
             <span class="a-size-medium a-color-base a-text-normal">
              The Acta Pilati: Important Testimony of Pontius Pilate, Recently Discovered, Being His Official Report to the Emperor Tiberius, Concerning the Crucifixion of Christ (Classic Reprint)
             </span>
            </a>

"""