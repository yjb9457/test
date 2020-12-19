from selenium import webdriver
import time
import pandas as pd


# source : https://github.com/sehwaa/Mangoplate-Crawling + 예외 처리문, 일시정지 함수, 클릭 함수,
# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome(r'C:\Users\yjb10\Desktop\python\workspace\chromedriver.exe')

# 구글 지도 접속하기
driver.get("https://www.google.com/maps/")

# '검색창에 음식점 검색'을 위해
searchbox = driver.find_element_by_css_selector("input#searchboxinput") # 페이지 개발 도구를 이용해 특정 부분 소스를 가져옴
searchbox.send_keys(input("음식점 검색: ")) # 검색창에 '음식점 검색'이란 문장을 입력받음
time.sleep(3) # 일시정지 함수: 과부하를 막기 위해 틈틈히 넣어둠

# '검색버튼 클릭'을 위해
searchbutton = driver.find_element_by_css_selector("button#searchbox-searchbutton") #검색 버튼 소스
searchbutton.click()
time.sleep(3)

# '필터더보기버튼 클릭'을 위해
button = driver.find_element_by_xpath('//button[@aria-label="필터 더보기"]') #필터 더보기 버튼 xpath 소스
button.click()
time.sleep(3)

# '영업중 버튼 클릭'을 위해
open = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[3]/div[2]/div[2]/input') #영업중 버튼 xpath 소스
open.click()
time.sleep(3)

# '완료 버튼 클릭'을 위해
complete = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[1]/div[3]/button[2]') #완료 버튼 xpath 소스
complete.click()
time.sleep(3)

result = [] #결과를 리스트로 저장할 것
# 여러 페이지(999)에서 반복하기(페이지가 몇개있는지 모르니 일단 999로 설정함)
for i in range(999): #999페이지 이하의 페이지에서 아래 함수들이 반복됨
    time.sleep(5)

    # 컨테이너(가게) 데이터 수집 // div.section-result-content
    stores = driver.find_elements_by_css_selector("div.section-result-content")

    for s in stores:
        # 가게 이름 데이터 수집 // h3.section-result-title

        title = s.find_element_by_css_selector("h3.section-result-title").text # 수집한 데이터는 text로 전환

        # 영업 시간 데이터 수집 // span.section-result-info.section-result-opening-hours

        time1 = s.find_element_by_css_selector("span.section-result-info.section-result-opening-hours").text

        # 평점 데이터 수집 // span.cards-rating-score

        score = s.find_element_by_css_selector("span.cards-rating-score").text


        # 가게 주소 데이터 수집 // span.section-result-location

        addr = s.find_element_by_css_selector("span.section-result-location").text
        print(title, "|", time1, "|", score, "|", addr)
        result.append([title, time1, score, addr]) #결괏값을 리스트로 정렬

    # 다음페이지 버튼 클릭 하기
    # 다음페이지가 없는 경우(데이터 수집 완료) 프로그램 종료
    try:
        nextpage = driver.find_element_by_css_selector("button#n7lv7yjyC35__section-pagination-button-next")
        nextpage.click()
    except:
        print("데이터 수집 완료.")
        break

    # Source: https://wikidocs.net/43282
    # 불러온 결괏값을 데이터프레임을 이용해 'cafe_around_ajou'라는 이름의 csv파일로 저장함
    df = pd.DataFrame(result, columns=['이름', '시간', '평점', '주소'])
    df2 = df.sort_values(by='평점', axis=0, ascending=False)  # 컬럼 '평점'을 내림차순으로 정렬(cf. 오름차순은 ascending=True)
    df2.to_csv('cafe_around_ajou_.csv', index=False, encoding='cp949') #파이썬 기본 인코딩이 utf-8이라 encoding='cp949'를 입력해주지 않으면 에러가 뜸




# 크롬창 닫기
# driver.close()

#https://wikidocs.net/43280