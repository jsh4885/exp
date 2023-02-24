from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import pandas as pd

# 스크랩 할 URL
gm_url = 'http://corners.gmarket.co.kr/bestsellers'

# 불필요한 로그를 제거하기 위해 ChromeOptions 개체 만들기
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 컨텍스트 관리자를 사용하여 webdriver 열기
with webdriver.Chrome(options=options) as driver:
    try:
        driver.get(gm_url)

        # 요소가 로드될 때까지 대기
        global itemNames, itemPrices
        itemNames = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'itemname')))

        itemPrices = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 's-price')))

    except TimeoutException:
        print("Timeout occurred while waiting for elements")
        driver.quit()
        # 프로그램을 종료하거나 오류 메시지를 반환합니다.
    except WebDriverException as e:
        print("Error occurred while getting elements:", e)
        driver.quit()
        # 프로그램을 종료하거나 오류 메시지를 반환합니다.

    # 항목 이름과 가격을 저장할 빈 목록 만들기
    itemNames_list = []
    itemPrice_list = []

    # 항목을 반복하고 이름과 가격을 얻습니다
    for item_name, item_price in zip(itemNames, itemPrices):
        itemNames_list.append(item_name.text)
        itemPrice_list.append(item_price.text)

    # 목록에서 사전을 만들고 DataFrame으로 변환
    item_dic = {"상품명": itemNames_list, "가격": itemPrice_list}
    item_df = pd.DataFrame(item_dic)

    # "가격" 열에서 숫자만 추출하여 새로운 "가격(숫자)" 열 생성
    item_df["가격(숫자)"] = item_df["가격"].str.replace(",", "").str.extract("(\d+)")
    item_df["가격(숫자)"] = pd.to_numeric(item_df["가격(숫자)"])

    # "가격" 열을 숫자+원 형태로 변환
    item_df["가격"] = item_df["가격(숫자)"].apply(lambda x: "{:,}원".format(x))

    # "가격(숫자)" 열 삭제
    item_df = item_df.drop("가격(숫자)", axis=1)

    # DataFrame 인쇄
    print(item_df)
