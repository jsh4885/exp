from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

gm_url = 'http://corners.gmarket.co.kr/Bestsellers'
driver = webdriver.Chrome()
driver.get(gm_url)

itemNames_list = []
itemPrice_list = []
tagNames_list = []

def collect_items(driver, tagName):
    while True:
        try:
            itemNames = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'itemname')))

            itemPrices = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 's-price')))
            break
        except:
            driver.refresh()
            time.sleep(1)

    for item_name, item_price in zip(itemNames, itemPrices):
        itemNames_list.append(item_name.text)
        itemPrice_list.append(item_price.text)
        tagNames_list.append(tagName)

    # Scroll down to load the next list
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Call collect_items() function to collect the next list
    if driver.find_elements(By.CSS_SELECTOR, 'div#footer'):
        return
    collect_items(driver, tagName)

tabs = driver.find_elements(By.CSS_SELECTOR, '#categoryTabG > li')
for i in tqdm(range(1, len(tabs))):
    tabs = driver.find_elements(By.CSS_SELECTOR, value='#categoryTabG > li')
    tagName = tabs[i].text

    driver.execute_script("arguments[0].click();", tabs[i])

    collect_items(driver, tagName)


# Create a dictionary from the list and convert it to a DataFrame
item_dic = {"Tag": tagNames_list, "상품명": itemNames_list, "가격": itemPrice_list}
item_df = pd.DataFrame(item_dic)

# Extract numbers from the "가격" column and create a new "가격(숫자)" column
item_df["가격(숫자)"] = item_df["가격"].str.replace(",", "").str.extract("(\d+)").astype(float)

# Convert the "가격" column to the format of number+KRW
item_df["가격"] = item_df["가격(숫자)"].apply(lambda x: "{:,.0f}원".format(x))

# Drop the "가격(숫자)" column
item_df = item_df.drop("가격(숫자)", axis=1)

print(item_df)

# DataFrame 저장
item_df.to_csv('item_list.csv', index=False)

driver.quit()
