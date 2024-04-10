from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

os.system('clear')

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)

url_base = 'https://www.amazon.com/'
main_route = 's?i=stripbooks&rh=n%3A283155%2Cp_30%3AForgotten+Books%2Cp_n_feature_browse-bin%3A2656022011&s=exact-aware-popularity-rank&dc&language=pt&ds=v1%3AF62MM2U5pQxy5ihMMkiYz3DXl5SKe%2FaUTy9uSUSDxkc&Adv-Srch-Books-Submit.x=35&Adv-Srch-Books-Submit.y=4&qid=1712363856&unfiltered=1&ref=sr_st_exact-aware-popularity-rank'
driver.get(url_base + main_route)
sleep(2)

pagination = driver.find_element(By.XPATH,"//span[@class='s-pagination-item s-pagination-disabled']")
num = int(pagination.text)
print(num - 1)

for page in range(num - 1):
    print("URL atual:", driver.current_url)
    name_elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")))
    index = 1
    print("URL atual:", driver.current_url)
    for name_element in name_elements:
        try:
            print(name_element.text)  
            name_element.click()
            WebDriverWait(driver, 10).until(EC.url_changes)  
            print(f"Anúncio {index}")
            driver.back()
            WebDriverWait(driver, 10).until(EC.url_changes)  
            index += 1
        except Exception as e:
            print(f"Erro ao interagir com o elemento: {e}")
            continue
    sleep(2)

    try:
        print("URL atual:", driver.current_url)
        next_button = driver.find_element(By.XPATH, "//a[contains(@class, 's-pagination-item') and contains(text(), 'Próximo')]")
        next_button.click()
        print("Página:", page + 2)
        WebDriverWait(driver, 10).until(EC.url_changes)  
        print("URL atual:", driver.current_url)
        sleep(10)
    except:
        print("O botão 'Next' não foi encontrado ou não é visível.")
        break

driver.quit()