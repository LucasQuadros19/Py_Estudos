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

name_element = driver.find_element(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")



name_element.click() 
sleep(5)

name_detail = driver.find_element(By.XPATH, "//span[@class='a-size-extra-large celwidget']")
price_detail = driver.find_element(By.XPATH, "//span[@class='a-size-medium a-color-price header-price a-text-normal']")
detail_section = driver.find_element(By.ID, 'detailBulletsWrapper_feature_div')

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
sleep(5)
driver.quit()
