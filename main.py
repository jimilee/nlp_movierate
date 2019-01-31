#def DataSet  데이터 분류, train, eval실행
from random import randint

strong, good, normal, bad = [], [], [], []
def DevData():
    files = ['./data/data1.txt','./data/data2.txt','./data/data3.txt','./data/data4.txt','./data/data5.txt']
    score = [strong, good, normal, bad]
    start = [0, int(len(strong)/5), int(len(strong)/5*2), int(len(strong)/5*3), int(len(strong)/5*4)]
    cnt = 0
    for name in files:
        file = open(name,'w',encoding='utf-8')
        for sc in score:
            for line in range(start[cnt], start[cnt]+1905):
                try:
                    file.write(sc[line])
                except:
                    file.write(sc[randint(start[cnt], start[cnt]+1905)])
        cnt += 1




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
                file_dev.write(sc[randint(0, len(sc)-1)])

    file.close()
    file_dev.close()
def DataSet():
    file = open('./data/train.txt', 'r',encoding='utf-8')

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
    file.close()


DataSet()
#Equalize(max,10)
DevData()