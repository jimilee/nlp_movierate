#def DataSet  데이터 분류, train, eval실행
from random import randint
strong, good, normal, bad = [], [], [], []

def Equalize(type, dev):
    counts =[len(strong), len(good), len(normal), len(bad)]
    score = [strong, good, normal, bad]
    file = open('./data/train.txt','w',encoding='utf-8')
    file_dev = open('./data/dev.txt', 'w', encoding='utf-8')
    for sc in score:
        for i in range(0, int(type(counts) * dev/10)):
            try:
                file.write(sc[i])
            except: #범위를 넘는 경우, 자신의 배열에서 랜덤 복사
                file.write(sc[randint(0,len(sc)-1)])

        for j in range(int(type(counts)*dev/10 + 1), type(counts)):
            try:
                file_dev.write(sc[j])
            except:
                file_dev.write(sc[randint(0,len(sc)-1)])


def DataSet():
    file = open('dataset.txt', 'r',encoding='utf-8')

    for line in file:
        cls = line.split(',')[1]
        if cls =="강추\n":
            strong.append(line)
        if cls == "추천\n":
            good.append(line)
        if cls == "보통\n":
            normal.append(line)
        if cls == "비추천\n":
            bad.append(line)

    print("counts= 강추 :", len(strong)," 추천 : ", len(good), " 보통 : ", len(normal), " 비추천 : ", len(bad))

DataSet()
Equalize(max,8)