from django.db import models
from .models import Question
def addSql(_QID,_Body,_Unit,_Old,_Number):  #增
    Q = Question(QID=_QID,Body=_Body,Unit=_Unit,Old=_Old,Number=_Number)
    Q.save()
    Question.objects.all()      #调试用

def delSql(_QID):                           #删
    Q = Question.objects.get(QID=_QID)
    Q.delete()
    Question.objects.all()

def modSql(_QID,_Body,_Unit,_Old,_Number):  #改
    Q = Question.objects.get(QID=_QID)
    Q.Body=_Body
    Q.Unit=_Unit
    Q.Old=_Old
    Q.Number=_Number
    Q.save()
    Question.objects.all()

def srhSql(_QID=-1):                             #查
    if _QID==-1:                                #若缺省则随机查找
        return Question.objects.get(random.randint(0,Question.objects.count()))
    else:                                       #否则按照Id查找
        return Question.objects.get(QID=_QID)




