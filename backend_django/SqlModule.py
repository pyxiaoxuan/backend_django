from django.db import models
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR+'\\backend_django'))
from backend_django.models import Question
def addSql(_QID,_Body,_Type,_Unit,_TimeStamp,_Answer,_ChoiceA='NULL',_ChoiceB='NULL',_ChoiceC='NULL',_ChoiceD='NULL'):  #增
    Q = Question(QID=_QID,Body=_Body,Type=_Type,Unit=_Unit,TimeStamp=_TimeStamp,Answer=_Answer,ChoiceA=_ChoiceA,ChoiceB=_ChoiceB,ChoiceC=_ChoiceC,ChoiceD=_ChoiceD)
    Q.save()

def delSql(_QID):                           #删
    Q = Question.objects.get(QID=_QID)
    Q.delete()

def modSql(_QID,_Body,_Type,_Unit,_TimeStamp,_Answer,_ChoiceA='',_ChoiceB='',_ChoiceC='',_ChoiceD=''):  #改
    Q = Question.objects.get(QID=_QID)
    Q.Body=_Body
    Q.Type=_Type
    Q.Unit=_Unit
    Q.TimeStamp=_TimeStamp
    Q.Answer=_Answer
    Q.ChoiceA=_ChoiceA
    Q.ChoiceB=_ChoiceB
    Q.ChoiceC=_ChoiceC
    Q.ChoiceD=_ChoiceD
    Q.save()

def srhSql(_QID=-1):                             #查
    if _QID==-1:                                #若缺省则随机查找
        return Question.objects.get(random.randint(0,Question.objects.count()))
    else:                                       #否则按照Id查找
        return Question.objects.get(QID=_QID)




