import pandas as pd


# 이전 데이터프레임으로 저장한 csv파일 불러오기 / 파일명은 자신의 컴퓨터에 있는 경로로 입력
dining = pd.read_csv(r'C:\Users\yjb10\Desktop\python\workspace\cafe_around_ajou_.csv', encoding='cp949')
dining['평점'] = pd.to_numeric(dining['평점']) #특정 조건을 만족하는 행을 추출하기 위해 칼럼 '평점'의 서식을 숫자형으로 바꿔줌


# 결측값이 들어있으면 행 삭제하기 : https://rfriend.tistory.com/263
dining.dropna(inplace=True)#inplace=True를 입력한 이유는 따로 데이터프레임을 지정해서 저장하지 않고 바로 다음 함수에 적용시키기 위해서임

# Source : https://hogni.tistory.com/9
# 원하는 평점입력하기
while True:
    a = float(input("몇 점이상의 평점을 원하시나요?(1~5), 5점초과는 종료됩니다.:")) #평점을 실숫값으로 입력받기로 함
    highscore = dining['평점'] >= a #실숫값이 특정 값 이상일 경우의 데이터만 불러오기
    subset_dining = dining[highscore]
    print(subset_dining)


    if a > 5 : #입력값이 5 초과 시 프로그램 종료(break)
        print("프로그램을 종료합니다.")
        break