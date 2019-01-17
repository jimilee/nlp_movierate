from konlpy.tag import Kkma
from urllib.request import urlopen
#import requests
from bs4 import BeautifulSoup
kkma = Kkma()
getUrl = '{}'
def Data_Preprocessing():
    file = open('data.txt','r')
    file_result = open('data_preprocessed.txt','w')

    for line in file:
        nouns = kkma.nouns(line.split(',')[0])
        print(nouns)
        if(nouns != []):
            file_result.writelines(nouns +list(','+line.split(',')[1]))
            #file_result.write('\n')
def getData(url):

    webpage = urlopen(url)
    soup = BeautifulSoup(webpage, 'html.parser')
    file = open('data.txt','a')
    sentence = soup.select('div.reporter_line > dl > dd')
    score = soup.select('div.re_score_grp > div > div > em')

    for score_value, value in zip(score, sentence):
        print(value.text.strip(), score_value.text.strip())
        file.writelines(value.text.strip().replace(',',' ') +',\''+ score_value.text.strip() + '\'\n')


    small_sc = soup.select('li > div.star_score > em')
    small_se = soup.select('div.score_reple > p')

    for score_value, value in zip(small_sc, small_se):
        print(value.text.strip(), score_value.text.strip())
        file.writelines(value.text.strip().replace(',',' ') +',\''+ score_value.text.strip()+ '\'\n')

    file.close()

file = open('url.txt','r')

for url in file:
    print(url)
    getData(url)
file.close()

Data_Preprocessing()










