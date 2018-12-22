from django.db import models
from .models import Question
def addSql(_QID,_Body,_Unit,_Old,_Number):
    Q = Question(QID=_QID,Body=_Body,Unit=_Unit,Old=_Old,Number=_Number)
    Q.save()
    Question.objects.all()

def delSql(_QID):
    Q = Question.objects.get(QID=_QID)
    Q.delete()
    Question.objects.all()

def modSql(_QID,_Body,_Unit,_Old,_Number):
    Q = Question.objects.get(QID=_QID)
    Q.Body=_Body
    Q.Unit=_Unit
    Q.Old=_Old
    Q.Number=_Number
    Q.save()
    Question.objects.all()




