# 업무자동화연습 - 반병현 저
### 중요사항
1. 대부분의 파일은 저자의 코드
2. 연습하거나 직접 작성한 코드의 경우 '_tkim' 추가 (ex. sample_generator_tkim1.py)
3. 기본적으로 책을 그대로 따라가는게 아니라 스스로 더 편한 방향 추구 - '내'가 익숙한 자동화 추구
4. 원본 내용의 경우 fork된 bhban_rpa 리포지토리 확인

### 2022년 7월 16일
1. 회원 개인정보 파일 만들기 실습 - 경로 지정 시 os 대신 pathlib / Path 활용
2. 개인정보 파일을 텍스트 파일 하나로 합치기 실습 - shutil.copytree()를 통해 폴더 복사까지 코드로 진행
3. 개인정보 파일을 csv 파일 하나로 합치기 실습
4. 개인정보 파일을 csv 파일 예쁘게 합치기 실습
5. 개인정보 파일을 xlsx 엑셀 파일 하나로 합치기 실습 - 책 속 라이브러리 대신 openpyxl 활용
6. 예제용 csv 파일 만들기 실습 - csv 모듈 활용(DictWriter 등)
7. csv파일 1천개 양식 유지하며 하나로 합치기 실습 - csv 모듈 reader와 writer를 활용
8. 예제용 xlsx 파일 만들기 실습 - openpyxl 라이브러리 활용

### 2022년 7월 17일
1. xlsx 파일 1천개 양식 유지하며 하나로 합치기 실습 - openpyxl 활용
2. xlsx 파일 1천개 양식 유지하며 하나로 합치기 실습2 - pandas에서 pd.concat 기능 활용
3. 매크로 작성에서 책 저자 프로그램 대신 pyperclip 및 pyautogui를 활용(검색 시 많은 정보가 나오는 라이브러리 활용)
4. 화면 정보 빠르게 뽑아오기 실습 - pyautogui 활용
5. 매크로를 활용해 로그인 구현 실습 - sys.argv[]와 클래스에 대한 이해도 상승 필요

### 2022년 7월 18일
1. 매크로를 활용해 뉴스기사 트위터 업로드 실습 - 트위터 업로드 대신 엑셀로 변환하는 방향으로 전환
2. openpyxl의 여러가지 기능 활용 - font, alignment 및 중첩 for문 활용 등. 추후 array형태의 업로드도 고려

### 2022년 7월 19일
1. 매크로 없이 트위터 로그인 구현 실습 - 트위터 대신 네이버 로그인으로 변환하여 코드 작성
2. 매크로 없이 뉴스 기사 트위터 업로드 실습 - 일단 jupyter notebook에서 여러모로 실습 하는 중

### 2022년 7월 20일
1. 매크로 없이 뉴스기사 트위터 업로드 실습 - 트위터 업로드 대신 엑셀로 변환하는 방향으로 전환. 책 내용 대신 나만의 코드로 일단 작성
  - class의 이해도가 더 높아져야.. (메서드에서 'self.'를 넣어야 할 때와 넣지 않아도 될 때를 구분 필요)
  - 책에 있는 코드로도 해본 후 나한테 더 맞는게 무엇인지(확장성)을 고려할 필요

### 2022년 7월 21일
1. 코딩보다 Selenium 중요 함수 등 습득(크롬 드라이버에서 여러 개의 탭을 실행하는 법)
  - driver.execute_script("window.open('');")
  - new_tab = driver.window_handles[-1]
  - driver.switch_to.window(new_tab)
  - driver.get(url)
2. 다음 복습은 뚝딱뚝딱 파이썬 자동화 복습 이후로 예정

### 2022년 8월 29일
1. 회원 개인정보 파일 만들기 실습 - 경로 지정 시 Path 활용 + string 모듈 활용
2. 개인정보 파일을 텍스트 파일 하나로 합치기 실습 - shutil.copytree()를 통해 폴더 복사까지 코드로 진행
3. 개인정보 파일을 csv 파일 예쁘게 합치기 실습 - split()을 활용해 csv 형식에 맞게 변경

### 2022년 8월 30일
1. 개인정보 파일을 xlsx 엑셀 파일 하나로 합치기 실습 - 책 속 라이브러리 대신 openpyxl 활용
2. 예제용 csv 파일 만들기 실습 - csv 모듈 대신 일반 텍스트 형태 활용

### 2022년 8월 31일
1. csv파일 1천개 양식 유지하며 하나로 합치기 실습 - csv 모듈 reader와 writer를 활용
2. 예제용 xlsx 파일 만들기 실습 - openpyxl 라이브러리 활용
3. xlsx 파일 1천개 양식 유지하며 하나로 합치기 실습2 - pandas에서 pd.concat 기능 활용

### 2022년 9월 1일
1. 매크로 작성에서 책 저자 프로그램 대신 pyperclip 및 pyautogui를 활용
2. 매크로를 활용해 로그인 구현 실습 - 완료하고 나면 왜 꺼지지.. 안꺼지는게 좋은데..
3. 매크로를 활용해 뉴스기사 엑셀 변환 실습 - 우여곡절이 많았으나 어쨌든 완료

### 2022년 9월 2일
1. 매크로 없이 네이버, 다음 로그인 구현 실습 - find_element(By.NAME, 'id') 등 이용
2. 매크로 없이 뉴스기사 엑셀 저장 실습. 책 내용 대신 나만의 코드로 작성 - 링크까지 추출(.attrs 속성)

### 2022년 9월 3일
1. 코딩보다 Selenium 중요 함수 등 습득(크롬 드라이버에서 여러 개의 탭을 실행하는 법)
  - driver.execute_script("window.open('');")
  - new_tab = driver.window_handles[-1]
  - driver.switch_to.window(new_tab)
  - driver.get(url)
2. 이번 학습사항 전체 빠른 복습 진행 - openpyxl, pyautogui, selenium 등
3. 타 교재(automation_practice-sweigart) 간단 학습을 통한 적용여부 파악
  - re.compile()로 대표되는 정규표현식(search, findall, sub 메서드)
  - Path, os, shutil 등으로 대표되는 경로 파악(cf. Path.cwd() == Path('.'), 상위폴더는 '..')
  - (os.walk()의 경우 folder_name, subfolders, filenames의 튜플로 분리 가능)
  - requests, BeautifulSoup, selenium 등으로 대표되는 웹 크롤링/스크래핑
  - (bsObj.find_all('img', {'class':'xxx'})[0].get('title') 과 같이 get() 메서드 활용 가능)
  - openpyxl 및 gspread의 기초 비교, PyPDF2 라이브러리 등 엑셀, 구글스프레드시트, PDF파일 컨트롤
  - 시간관리(time, datetime, timedelta 등) 및 프로그램 실행 기초(subprocess, threading)
  - email 모듈 및 smtplib 모듈 활용하여 이메일 보내기