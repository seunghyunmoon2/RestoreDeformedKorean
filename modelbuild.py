# -*- coding: utf-8 -*-

# !pip install KoSpacing

# from hangul_utils import Preprocessor
# p = Preprocessor()
# p.normalize("부들부들부들부들 내가 작간데 화가낰ㅋㅋㅋㅋ")
# #"부들부들 내가 작가인데 화가나ㅋㅋㅋ"

# from hangul_utils import normalize
# normalize("부들부들부들부들 내가 작간데 화가낰ㅋㅋㅋㅋ")
# #"부들부들 내가 작가인데 화가나ㅋㅋㅋ"



'''
1. fetch comments a CSV file from 
2. 
3.
4.
5.

'''



# unicode.py 실행 필요.

'''is_hangul_syllable('갍')
Out[6]: True'''

cmt = """
요번에 오랜만에 외국여행을 친구들이랑 왔는데 여기 집주인이 아주 아니에요. 가격도 그렇게 싼 편이 아닌데 서비스가 엉망이고요, 화장실도 더럽고 우리가 뭐라 하니 화만 내네요 ㅠ.ㅠ 여기 주변 음식점도 다 맛 없고 분위기도 별로에요.

여기 리뷰 잘 써주면 할인해준다고는 해서 쓰고있는데 이 리뷰 보시고 다들 잘 거르시길 바랍니다...
"""

# 이제 문장 붙이고, 해보

import re
nospacecmt = re.sub('[ \n]','',cmt)
nospacecmt

split_syllables(nospacecmt)




# def fetch_from_Godsejong(processed): # processed cmt from PREPORCESS_COMMENT
from selenium import webdriver
driver = webdriver.Chrome('/home/seunghyunmoon/Documents/chromedriver') # PC 디렉토리
resp = driver.get('https://thtl1999.github.io/God-sejong/')
print(driver.find_element_by_xpath('//*[@id="addPraise"]'))
driver.quit()


# import csv
# with open('./full_test1.csv','w+',newline='') as f:
#     write = csv.writer(f)
#     write.writerows(['요번에','친구들이랑','간만에'])

# with open('./full_test1.csv', newline='') as f:
#     read = csv.reader(f,delimiter=' ',quotechar='|')
#     ss = ''
#     for row in read:
#         ss+=''.join(row)
#     print(ss)    
# import re
# with open('./full_test1.csv', newline='') as f:
#     read = csv.reader(f,delimiter=' ',quotechar='|')
#     for row in read:
#         print(re.sub(',','',row[0]))

# kk =[]
# with open('./full_test.csv', newline='')as f:
#     read = csv.reader(f,delimiter=' ',quotechar='|')
#     for row in read:
#         kk = row
#         print(row)
#         break
converted =[]
with open('./full_test.csv', newline='')as f:
    read = csv.reader(f,delimiter=' ',quotechar='|')
    for row in read:
        converted.append(row)
print(len(converted))
        
# #pp = ''.join(kk[0].split(','))
# pppp = re.sub('\W','',kk[0]) 
# pppppp = set(split_syllables(pppp)

             
# pre1 = ''
# for i in range(len(converted)-1):
#     pre1 += re.sub('\W','',converted[i][0])
    
# pre1_set = set(split_syllables(pre1))
             
# han_char = {}
# for cnt, p in enumerate(pppppp):
#     han_char[p] = cnt

pre2_set

pre2 = ''
for i in range(len(converted)-1):
    pre2 += re.compile('[^ㄱ-ㅣ가-힣]').sub('',converted[i][0])
    
print(len(pre2))
pre2_set = sorted(list(set(split_syllables(pre2))))


# 4
han2char = {}             
for cnt, char in enumerate(pre2_set):
    han2char[char] = cnt






# dictionary 만들어준다.
1. fecth a cmt from csv
2. convert it by split_syllables
#3. check if exists in the dictionary: pass else: update with a key value
4. ready to use as input to our model.


for x in 'ㅐㅖㅘㅙㅚㅝㅞㅟㅢㅔㅒ':
    cnt = 48
    if x in han2char:
        print(x, 'yes')
    else:
        print(x, 'no, update dictionary')
        han2char[x] = cnt
        cnt += 1


#기억나지 않습니다...