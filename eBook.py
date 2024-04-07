from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = webdriver.SafariOptions()
options.headless = True
driver = webdriver.Safari(options=options)

url_base = 'https://www.amazon.com/'
mainRoute = 's?i=stripbooks&rh=n%3A283155%2Cp_30%3AForgotten+Books%2Cp_n_feature_browse-bin%3A2656022011&s=exact-aware-popularity-rank&dc&language=pt&ds=v1%3AF62MM2U5pQxy5ihMMkiYz3DXl5SKe%2FaUTy9uSUSDxkc&Adv-Srch-Books-Submit.x=35&Adv-Srch-Books-Submit.y=4&qid=1712363856&unfiltered=1&ref=sr_st_exact-aware-popularity-rank'
driver.get(url_base + mainRoute)
sleep(2)

# Aguardar até que os resultados estejam disponíveis
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 's-result-item')))

# Extrair o nome do primeiro item da lista
name_element = driver.find_element(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
name = name_element.text

# Clicar no primeiro item para ir para a página de detalhes
name_element.click()
sleep(5)

# Extrair detalhes do livro
detail = driver.find_element(By.ID, 'detailBulletsWrapper_feature_div')
ul = detail.find_element(By.CLASS_NAME, 'a-unordered-list')
lis = ul.find_elements(By.TAG_NAME, 'li')

# Extrair o texto do segundo span de cada lista
for li in lis:
    spans = li.find_elements(By.TAG_NAME, 'span')
    if len(spans) >= 2:
          print("Texto do segundo span: 2", spans[2].text.strip())

# Fechar o navegador
driver.quit()
