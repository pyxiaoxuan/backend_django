from django.db import models
from backend_django.models import Question
import random
import json

DUP_SPAN = 3
TOTAL_NUM = [10,10,4,5]
TYPE_LABEL = ["Choice","Completion","Calcution","Essay"]
CurrentTimestamp = 255
ABType = "B"

def getpaper(threshold = None, cal_unit = None, essay_unit = None):

    if threshold is None:
        threshold = 0.3
    
    if cal_unit is None or not isinstance(cal_unit,list) or len(cal_unit) != 4:
        cal_unit = [1,2,3,4]
    if essay_unit is None or not isinstance(essay_unit,list) or len(essay_unit) != 5:
        essay_unit = [1,2,3,4,5]
    global CurrentTimestamp,ABType
    
    CurrentTimestamp += 1

    if ABType == "A":
        ABType = "B"
    else:
        ABType = "A"
    #print(threshold)
    #print(cal_unit)
    #print(essay_unit)
    #choice_num,completion_num,calculation_num,essay_num
    

    #now = datetime.now().strftime("%Y-%m-%d")
    paper = {"Subject":"数据结构","ABType":ABType}
    for Type in range(len(TOTAL_NUM)):
        #print(Type)
        dup_count = 0 #duplicate count
        content = []
        num = TOTAL_NUM[Type]
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
                qid = i+1
            else:
                if Type == 3:
                    unit = essay_unit[i]
                    qid = i+1
                else:
                    unit = 0
                    qid = 0
            if r < p :
                content.append(qryDupQuestion(Type,unit,qid))
                dup_count += 1
            else :
                content.append(qryNewQuestion(Type,unit,qid))
        if Type < 2 :
            random.shuffle(content)
        paper[TYPE_LABEL[Type]] = content

    #print(paper)
    paper = json.dumps(paper, ensure_ascii=False)
    #print(paper)
    return paper

def qryDupQuestion(Type,unit,qid):

    Q = Question.objects.all()
    for q in Q:
        if unit != 0 and unit != int(q.Unit):
            continue
        if Type != int(q.Type):
            continue
        if qid != int(q.QID):
            continue
        if int(q.TimeStamp) == CurrentTimestamp or not collapse(int(q.TimeStamp)):
            continue
        q.TimeStamp = str(CurrentTimestamp)
        q.save()
        return ModeltoJson(q)
    return qryNaiveQuestion(Type,unit,qid)

def qryNewQuestion(Type,unit,qid):

    Q = Question.objects.all()
    for q in Q:
        if unit != 0 and unit != int(q.Unit):
            continue
        if Type != int(q.Type):
            continue
        if qid != int(q.QID):
            continue
        if int(q.TimeStamp) == CurrentTimestamp or collapse(int(q.TimeStamp)):
            continue
        q.TimeStamp = str(CurrentTimestamp)
        q.save()
        return ModeltoJson(q)
    return qryNaiveQuestion(Type,unit,qid)

def qryNaiveQuestion(Type,unit,qid):

    Q = Question.objects.all()
    for q in Q:
        if unit != 0 and unit != int(q.Unit):
            continue
        if Type != int(q.Type):
            continue
        if qid != int(q.QID):
            continue
        if int(q.TimeStamp) == CurrentTimestamp:
            continue
        q.TimeStamp = str(CurrentTimestamp)
        q.save()
        return ModeltoJson(q)
    #print(Type,unit,qid,"###")

def collapse(timestamp):
    if ABType == "A":
        return timestamp >= CurrentTimestamp - 2*DUP_SPAN
    else:
        return timestamp >= CurrentTimestamp - 2*DUP_SPAN - 1 and timestamp < CurrentTimestamp - 1

def ModeltoJson(m):
    if m.Type == "0":
        return {"Question":m.Body,"ChoiceA":m.ChoiceA,"ChoiceB":m.ChoiceB,"ChoiceC":m.ChoiceC,"ChoiceD":m.ChoiceD,"Answer":m.Answer}
    else:
        return {"Question":m.Body,"Answer":m.Answer}

CUT_LENGTH = 20

def cut(str):
    return str[:CUT_LENGTH]

def getBody(Type):
    Type = int(Type)
    Q = Question.objects.all()
    Json = []
    for q in Q:
        if Type != int(q.Type):
            continue
        Json.append({"title":cut(q.Body),"id":q.id})
    Json = json.dumps(Json, ensure_ascii=False)
    #print(Json)
    return Json

def init():
    Q = Question.objects.all()
    for q in Q:
        q.TimeStamp = "0"
        q.save()

'''
init()
getpaper()
getBody("2")
'''