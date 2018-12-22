# coding: utf-8
from django.db import models

# Create your models here.
class Question(models.Model):
    QID=models.CharField(max_length=70)          #题目序号
    Body=models.TextField()                     #题目内容
    Unit=models.CharField(max_length=10)        #题目单元
    Old=models.CharField(max_length=2)          #是否出现过
    Number=models.CharField(max_length=70)      #识别号
    def __str__(self):
        return self.Body
    '''
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
    '''