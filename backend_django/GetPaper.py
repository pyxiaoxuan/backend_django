from SqlModule import addSql,modSql,delSql
import random
timestamp = 0

def getpaper(n,k): #total number, threshold
    global timestamp
    timestamp += 1

    paper = []
    j = 0 #duplicate count
    for _ in range(1,n):
        p = (k-j)/n
        print(p)
        r = random.random()
        if r < p :
            #paper.append(qryDupQuestion(timestamp))  TODO
            j += 1
        else :
            j += 0 #避免注释下一行之后报错
            #paper.append(qryNewQuestion(timestamp))  TODO
    assert j<=k
    return paper
