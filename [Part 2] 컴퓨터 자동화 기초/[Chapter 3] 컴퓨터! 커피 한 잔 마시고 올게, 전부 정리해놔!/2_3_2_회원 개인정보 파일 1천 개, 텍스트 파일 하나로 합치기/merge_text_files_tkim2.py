from pathlib import Path
import os
import shutil

p1 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_1_회원 개인정보 파일 1천 개, 1초만에 만들기' / 'personal_info_tkim2'
p2 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_2_회원 개인정보 파일 1천 개, 텍스트 파일 하나로 합치기' / 'personal_info_tkim2'
p3 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_2_회원 개인정보 파일 1천 개, 텍스트 파일 하나로 합치기'

# shutil.copytree()의 경우 동일한 경로에 해당 폴더가 있으면 에러 발생
try:
    shutil.copytree(p1, p2)
except:
    print('이미 존재하는 폴더입니다.')

outfile_name = 'merged_ID_tkim2.txt'

# os.listdir() 함수를 통해 폴더의 내용물을 list 형태로 가공
files = os.listdir(p2)

with open(p3 / outfile_name, mode='w') as write_file:
    for filename in files:
        if '.txt' not in filename:
            continue
        read_file = open(p2 / filename, mode='r')
        contents = read_file.read()
        write_file.write(f'{contents}\n\n')

print('Process Done!')
