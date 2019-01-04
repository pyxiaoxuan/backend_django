from django.db import models
from backend_django.models import Question

#from .SqlModule import addSql,modSql,delSql
#from __future__ import division
import random
import json
from datetime import datetime

DUP_SPAN = 3
TOTAL_NUM = [10,10,4,5]
TYPE_LABEL = ["Choice","Completion","Calcution","Essay"]
CurrentTimestamp = 1
ABType = "A"

def getpaper(threshold = None, cal_unit = None, essay_unit = None):

    if threshold is None:
        threshold = 0.3
    
    if cal_unit is None or not isinstance(cal_unit,list) or len(cal_unit) != 4:
        cal_unit = [1,2,3,4]
    if essay_unit is None or not isinstance(essay_unit,list) or len(essay_unit) != 5:
        essay_unit = [1,2,3,4,5]
    global CurrentTimestamp,ABType
    
    #print(threshold)
    #print(cal_unit)
    #print(essay_unit)
    #choice_num,completion_num,calculation_num,essay_num
    

    #now = datetime.now().strftime("%Y-%m-%d")
    paper = {"Subject":"数据结构","ABType":ABType}
    for Type in range(len(TOTAL_NUM)):
        print(Type)
        dup_count = 0 #duplicate count
        content = []
        num = TOTAL_NUM[i]
        for i in range(num):

            if Type == 0 or Type == 1:
                p = int(threshold*num)
                p = float(max(p-dup_count,0))
                #print(p)
                p /= num
                #print(p)
                #print("###")

            else:
                p = 0
            #print(p)
            r = random.random()+0.0001 #r:[0.0001,1.0001]
            if Type == 2:
                unit = cal_unit[i]
            else:
                if Type == 3:
                    unit = essay_unit[i]
                else:
                    unit = 0
            if r < p :
                content.append(qryDupQuestion(Type,unit))
                dup_count += 1
            else :
                content.append(qryNewQuestion(Type,unit))
        paper[TYPE_LABEL[Type]] = content

    if ABType == "A":
        ABType = "B"
    else:
        ABType = "A"
        CurrentTimestamp += 1
    print(paper)
    return paper

def qryDupQuestion(Type,unit):

    Q = Question.objects.all()
    for q in Q:
        if unit != 0 and unit != q.Unit:
            continue
        if Type != q.Type:
            continue
        q.TimeStamp = CurrentTimestamp
        q.save()
        return q

def qryNewQuestion(Type,unit):

    Q = Question.objects.all()
    for q in Q:
        if unit != 0 and unit != q.Unit:
            continue
        if Type != q.Type:
            continue
        if q.TimeStamp != CurrentTimestamp and q.TimeStamp > CurrentTimestamp - DUP_SPAN:
            continue
        q.TimeStamp = CurrentTimestamp
        q.save()
        return q

getpaper(0.4,[1,2,3,2],[1,2,3,3,5])
getpaper(0.4,[1,2,3,2,3],[1,2,3,3,5])
getpaper(0.4,[1,2,3,2],3)
getpaper()