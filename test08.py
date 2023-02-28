from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from urllib.request import urlretrieve
from tqdm import tqdm

# 상수 정의
IMAGE_DIRECTORY = os.path.abspath("./이미지")

def download_images_from_naver(keyword, num_images):
    # 네이버 이미지 검색 URL 생성
    naver_search_url = f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}"

    # 웹 드라이버 설정
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 페이지 로딩 대기
    wait = WebDriverWait(driver, 10)
    driver.get(naver_search_url)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div > div.thumb > a > img")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div > div.thumb > a > img")))

    # 이미지 URL 추출
    images = driver.find_elements(By.CSS_SELECTOR, "div > div.thumb > a > img")
    image_url_list = []
    for i in tqdm(range(num_images)):
        img_url = images[i].get_attribute("src")
        if "data:" in img_url:
            continue
        image_url_list.append(img_url)

    # 이미지 다운로드
    if not os.path.isdir(IMAGE_DIRECTORY):
        os.makedirs(IMAGE_DIRECTORY)

    for idx, src_url in tqdm(enumerate(image_url_list, 1)):
        try:
            file_name = f"{keyword}_{idx}.jpg"
            file_path = os.path.join(IMAGE_DIRECTORY, file_name)
            if not os.path.isdir(os.path.dirname(file_path)):
                os.makedirs(os.path.dirname(file_path))
            urlretrieve(src_url, file_path)
        except Exception as e:
            print(f"Error occurred while downloading {src_url}: {e}")
            continue

    # 웹 드라이버 종료
    driver.quit()

download_images_from_naver("군산", 10)
