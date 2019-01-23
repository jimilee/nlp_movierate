from konlpy.tag import Kkma
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import HTTPError
#-*- coding: utf-8 -*-
kkma = Kkma() #Konlpy

#가져온 데이터에서 명사추출
def Data_Preprocessing():
    file = open('data.txt','r')
    file_result = open('./data/train.txt','w',encoding='utf-8')

    for line in file:
        try:
            nouns = kkma.nouns(line.split(',')[0])
            print(nouns)
            if(nouns != []):
                file_result.write(' '.join(nouns) +str(','+line.split(',')[1]))
        except:
            file_result.writelines("")
            print("pass")

#1 2 3 4 | 5 6 | 7 8 | 9 10 점수별
def setLabel(score):
    if score >= 9:
        return ',강추\n'
    if 9>score>= 7:
        return ',추천\n'
    if 7>score>=5:
        return ',보통\n'
    if 5>score>=0:
        return ',비추천\n'

def getData(url):

    try:
        webpage = urlopen(url)
        soup = BeautifulSoup(webpage, 'html.parser')
        file = open('data.txt','a')
        sentence = soup.select('div.reporter_line > dl > dd')
        score = soup.select('div.re_score_grp > div > div > em')

        for score_value, value in zip(score, sentence):
            print(value.text.strip(), score_value.text.strip())
            file.writelines(value.text.strip().replace(',', ' ').replace('\n',' ') + setLabel(float(score_value.text.strip())))

        small_sc = soup.select('li > div.star_score > em')
        small_se = soup.select('div.score_reple > p')

        for score_value, value in zip(small_sc, small_se):
            print(value.text.strip(), score_value.text.strip())
            file.writelines(value.text.strip().replace(',', ' ').replace('\n',' ') + setLabel(float(score_value.text.strip())))
        file.close()
    except HTTPError as e:
        print(e)
    else:
        return None


target = 'https://movie.naver.com/movie/bi/mi/point.nhn?code='
num = range(156742,200000)
# for i in num:
#     url = target+str(i)
#     print(url)
#     getData(url)


Data_Preprocessing()










