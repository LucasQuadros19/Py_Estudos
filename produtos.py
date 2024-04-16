import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.system('clear')

options = webdriver.FirefoxOptions()
options.headless = True
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

url_base = 'https://www.amazon.com/'
main_route = 's?i=stripbooks&rh=n%3A283155%2Cp_30%3AForgotten+Books%2Cp_n_feature_browse-bin%3A2656022011&s=exact-aware-popularity-rank&dc&language=pt&ds=v1%3AF62MM2U5pQxy5ihMMkiYz3DXl5SKe%2FaUTy9uSUSDxkc&Adv-Srch-Books-Submit.x=35&Adv-Srch-Books-Submit.y=4&qid=1712363856&unfiltered=1&ref=sr_st_exact-aware-popularity-rank'
driver.get(url_base + main_route)

pagination = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='s-pagination-item s-pagination-disabled']")))
num = int(pagination.text)
print(num - 1)

for page in range(num - 1):   
    name_elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")))
    
    for name_element in name_elements:
        try:
            print(name_element.text)
            name_element.click()

            name_detail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-size-extra-large celwidget']")))
            price_detail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-size-medium a-color-price header-price a-text-normal']")))
            detail_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'detailBulletsWrapper_feature_div')))

            uls = detail_section.find_elements(By.CLASS_NAME, 'a-unordered-list')

            if len(uls) >= 2:
                first_ul = uls[0]
                firstList_ul = first_ul.find_elements(By.TAG_NAME, 'li')
                second_ul = uls[1]
                secondList_ul = second_ul.find_elements(By.TAG_NAME, 'li')

            print("Book:", name_detail.text, price_detail.text)

            for i in range(1, len(firstList_ul)): 
                spans = firstList_ul[i].find_elements(By.TAG_NAME, 'span')
                if len(spans) >= 2:
                    print(spans[2].text.strip(), end=', ')

            # Print information from the second ul
            for li in secondList_ul:
                spans = li.find_elements(By.TAG_NAME, 'span')
                if spans:
                    for index, span in enumerate(spans):
                        print(f"[{index}] {span.text.strip()}", end=', ')
                else:
                    print("Two uls with the class 'a-unordered-list' were not found")

            driver.back()
        except Exception as e:
            print(f"Erro ao interagir com o elemento: {e}")
            continue

    try:
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 's-pagination-next')))
        next_button.click()
        WebDriverWait(driver, 10).until(EC.url_changes)
    except:
        print("O botão 'Next' não foi encontrado ou não é visível.")
        break

driver.quit()
