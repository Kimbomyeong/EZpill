import requests
from bs4 import BeautifulSoup
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import re
from selenium.common.exceptions import NoSuchElementException


def convert_to_mg(value):
    match = re.search(r'총\s*지\s*방\s*(\d+[.]?\d*\s*[a-z]*)', value, re.IGNORECASE)
    if match:
        total_fat = match.group(1)
        if total_fat.endswith('g'):
            numeric_value = float(total_fat.replace('g', ''))
            if numeric_value == 0:
                return "0mg"  # 만약 0g인 경우 0mg로 반환
            else:
                mg_value = numeric_value * 1000  # g를 mg로 변환
                return f"{mg_value}mg"
        elif total_fat.endswith('mg'):
            return total_fat

    match = re.search(r'콜\s*라\s*겐\s*(\d+[.]?\d*\s*[a-z]*)', value, re.IGNORECASE)
    if match:
        total_fat = match.group(1)

        if total_fat.endswith('m'):
        # 'm'으로 끝나는 경우
            numeric_value = total_fat.rstrip('m')
            if numeric_value.isdigit():  # 숫자로만 이루어진 경우에만 변환을 시도합니다.
                numeric_value = float(numeric_value)
                return f"{numeric_value}mg"
            else:
                return "숫자로 변환할 수 없는 값입니다."
            if total_fat.endswith('g'):
                numeric_value = float(total_fat.replace('g', ''))
                if numeric_value == 0:
                    return "0mg"  # 만약 0g인 경우 0mg로 반환
                else:
                    mg_value = numeric_value * 1000  # g를 mg로 변환
                    return f"{mg_value}mg"
        
            elif total_fat.endswith('mg'):
                return total_fat
        else:
            return match
    # 유산균 정보를 추출하는 정규 표현식 추가
    match = re.search(r'([\d,]+\.?\d*)\s*억\s*CFU(?![\w&])', value)
    if match:
        cfu_value = match.group(1).replace(',', '')  # 쉼표(,) 제거 후 CFU 값 추출
        return f"{cfu_value}억 CFU"
        

    match = re.search(r'([\d,]+\.?\d*)\s*([a-z]+)', value, re.IGNORECASE)
    if match:
        numeric_value_str = match.group(1).replace(',', '')  # 쉼표(,) 제거 후 숫자 값 추출
        if numeric_value_str:  # 빈 문자열이 아닌 경우에만 변환을 시도합니다.
            try:
                numeric_value = float(numeric_value_str)
                unit = match.group(2).strip().lower()  # 단위 추출 및 소문자로 변환

                # 단위에 따른 처리 코드 작성
                
            except ValueError:
                return "숫자로 변환할 수 없는 값입니다."
        else:
            return "숫자 값이 없습니다."  # 빈 문자열인 경우 처리
    


        if unit == 'mcg':
            mg_value = round(numeric_value / 1000, 3)  # mcg를 mg로 변환 (소수점 3자리까지)
            return f"{mg_value}mg"
        elif unit == 'mg':
            return f"{numeric_value}mg"
        elif unit == '%':
            return match.group(0)  # % 단위이면 원래 값 그대로 반환
        elif unit == 'ml':
            return f"{numeric_value}ml"
        elif unit == 'g':
            mg_value = numeric_value * 1000  # g를 mg로 변환
            return f"{mg_value}mg"
        elif unit == 'iu' or unit == 'i.u.' or unit == 'i.u':
            # 비타민 D의 경우의 변환 비율
            mg_value = numeric_value * 0.000025  
            return f"{mg_value:.8f}mg"  # 소수점 8자리까지 출력
        
    return match
        

query_txt = input('크롤링할 키워드는 무엇입니까?')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 브라우저 생성
browser = webdriver.Chrome(options=chrome_options)

browser.get("https://kr.iherb.com/")

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, "#txtSearch")
search.click()
time.sleep(2)

# 검색어 입력
search.send_keys(query_txt)

# 검색버튼 클릭
browser.find_element(By.CSS_SELECTOR, ".icon.icon-search").click()

# 페이지 로딩 대기
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".absolute-link.product-link")))

# 드롭다운 메뉴 버튼 요소를 찾습니다.
dropdown_menu = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.sort-by-relevance select.panel-form-control.dropdown-sort')))

# 드롭다운 메뉴를 클릭하여 옵션을 펼칩니다.
dropdown_menu.click()

# Select 객체를 생성합니다.
dropdown = Select(dropdown_menu)

# '평가 수가 많은' 옵션을 선택합니다.
dropdown.select_by_value('12')
time.sleep(3)

# 품절상품 숨기기
Out_of_stock_hidden = browser.find_element(By.CSS_SELECTOR, 'label[for="Filterooshideoutofstock"]')
browser.execute_script("arguments[0].click();", Out_of_stock_hidden)
time.sleep(5)

# 별점 5점 영양제 들어가기
ratings_5_filter = browser.find_element(By.CSS_SELECTOR, "#Filterratings5")
browser.execute_script("arguments[0].click();", ratings_5_filter)
time.sleep(3)
if query_txt=="유산균":
    ratings_4_filter = browser.find_element(By.CSS_SELECTOR, "#Filterratings4")
    browser.execute_script("arguments[0].click();", ratings_4_filter)
elif query_txt=="루테인":
    ratings_4_filter = browser.find_element(By.CSS_SELECTOR, "#Filterratings4")
    browser.execute_script("arguments[0].click();", ratings_4_filter)


# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(1)
    after_h = browser.execute_script("return window.scrollY")
    if after_h == before_h:
        break
    before_h = after_h

items = browser.find_elements(By.CSS_SELECTOR, "a.absolute-link.product-link")
item_links = [item.get_attribute('href') for item in items[:44]]

# CSV 파일 열기
with open('iherb_products콜라겐.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['Image_URL', 'Product_Title', 'Product_Manufacture', 'Product_Price', 'Product_Per_Price', 'Product_Usage', 'Product_Precautions', 'Product_Ingredient_Information', 'Review']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 헤더 작성
    writer.writeheader()

    for link in item_links:
        try:
            browser.get(link)

            # 페이지 로딩 대기
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-title")))

            # 크롤링 로직
            product_image = browser.find_element(By.CSS_SELECTOR, "#iherb-product-image").get_attribute("src")
            product_title = browser.find_element(By.CSS_SELECTOR, "h1#name").text
            product_manufacture = browser.find_element(By.CSS_SELECTOR, 'span[itemprop="name"] > bdi').text
            product_price = browser.find_element(By.CSS_SELECTOR, ".price-inner-text p").text.strip()
            product_per_price = browser.find_element(By.CSS_SELECTOR, ".small.price-per-unit").text.strip()
            product_description = browser.find_element(By.CSS_SELECTOR, 'div.row.item-row div[itemprop="description"]').text
            product_usage = browser.find_element(By.CSS_SELECTOR, '.col-xs-24 > .prodOverviewDetail p').text
            product_precautions = browser.find_element(By.CSS_SELECTOR, 'div.row.item-row:nth-child(4) > div.col-xs-24 > div.prodOverviewDetail').text
            try:
                product_ingredient_information = browser.find_element(By.CSS_SELECTOR, '.col-xs-24.col-md-10 .supplement-facts-container table').text

                # EPA와 DHA 문자열 존재 여부 확인 변수
                contains_epa_dha = any("EPA" in line or "DHA" in line for line in product_ingredient_information.split('\n'))

                if len(product_ingredient_information.split('\n')) > 5 and not contains_epa_dha and query_txt != "유산균" and '콜라겐' not in product_ingredient_information:
                    # 제품 설명이 5줄을 초과하고, EPA나 DHA 문자열을 포함하지 않는 경우, 다음 제품으로 넘어감
                    continue
                if query_txt == "유산균" and 'CFU' not in product_ingredient_information:
                    continue

            except NoSuchElementException:
                print("product_ingredient_information을 찾을 수 없습니다. 다음 제품으로 넘어갑니다.")
                continue

            # 변환된 영양 성분 정보 생성
            converted_info = convert_to_mg(product_ingredient_information)

            review_link = browser.find_element(By.CSS_SELECTOR, 'ugc-read-more[data-testid="pdp-qna-see-all-review"] > a')
            browser.execute_script("arguments[0].scrollIntoView();", review_link)
            browser.execute_script("arguments[0].click();", review_link)

            current_url = browser.current_url

            # 현재 페이지 URL에서 'sort=6'을 'sort=1'로 변경
            review_link = current_url.replace('sort=6', 'sort=1')

            browser.get(review_link)

            box_list = []

            boxes = browser.find_elements(By.CSS_SELECTOR, '.MuiBox-root.css-1v71s4n')

            for box in boxes:
                # 자세히 보기 버튼 클릭
                try:
                    more_btn = box.find_element(By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-body2.css-ptz5k')
                    browser.execute_script("arguments[0].click();", more_btn)
                    time.sleep(3)
                except:
                    continue

                try:
                    review = box.find_element(By.CSS_SELECTOR, '.MuiBox-root.css-0[data-testid="review-text"] a').text
                except:
                    review = "리뷰없음"

                box_item = {'Review': review}
                box_list.append(box_item)

            print("이미지 URL:", product_image)
            print("상품 제목:", product_title)
            print("제조사:", product_manufacture)
            print("상품 가격:", product_price)
            print("상품 개별가격:", product_per_price)
            print("상품 사용방법:", product_usage)
            print("상품 주의사항:", product_precautions)
            print("영양 성분정보:", converted_info )
            for item in box_list:
                print("리뷰:", item['Review'])
                print("=" * 200)


            # 각 제품의 리뷰를 줄 바꿈으로 연결하여 하나의 문자열로 변환
            reviews_str = "\n".join([item['Review'] for item in box_list])



            # CSV 파일에 쓰기 (리뷰 정보)
            
            writer.writerow({
                'Image_URL': product_image,
                'Product_Title': product_title,
                'Product_Manufacture': product_manufacture,
                'Product_Price': product_price,
                'Product_Per_Price': product_per_price,
                'Product_Usage': product_usage,
                'Product_Precautions': product_precautions,
                'Product_Ingredient_Information': converted_info ,
                'Review': reviews_str
            })

            time.sleep(2)  # 페이지 이동 후 대기
        except StaleElementReferenceException:
            print("StaleElementReferenceException 발생. 다음 항목으로 계속 진행합니다.")
            continue

# 브라우저 종료
browser.quit()