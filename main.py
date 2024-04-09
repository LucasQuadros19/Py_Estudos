from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = webdriver.SafariOptions()
options.headless = True
driver = webdriver.Safari(options=options)

url_base = 'https://www.amazon.com/'
main_route = 's?i=stripbooks&rh=n%3A283155%2Cp_30%3AForgotten+Books%2Cp_n_feature_browse-bin%3A2656022011&s=exact-aware-popularity-rank&dc&language=pt&ds=v1%3AF62MM2U5pQxy5ihMMkiYz3DXl5SKe%2FaUTy9uSUSDxkc&Adv-Srch-Books-Submit.x=35&Adv-Srch-Books-Submit.y=4&qid=1712363856&unfiltered=1&ref=sr_st_exact-aware-popularity-rank'
driver.get(url_base + main_route)
sleep(2)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 's-result-item')))

name_elements = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")

index = 1
for name_element in name_elements:
    name_element.click()
    sleep(2)
    print(f"Anúncio {index}")
    driver.back()
    sleep(2)
    index += 1

driver.quit()
