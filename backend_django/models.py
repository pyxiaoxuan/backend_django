# coding: utf-8
from django.db import models

# Create your models here.
class Question(models.Model):
    QID=models.CharField(max_length=70,default='wtxqqq')          #题目序号
    Body=models.TextField()                     #题面
    Type=models.CharField(max_length=10,default='wtxqqq')        #题目类别
    Unit=models.CharField(max_length=10,default='wtxqqq')        #题目单元
    TimeStamp=models.IntegerField(default=0)             #时间戳
    Answer=models.CharField(max_length=70,default='wtxqqq')      #答案
    ChoiceA=models.CharField(max_length=70,default='wtxqqq')      #A选项
    ChoiceB=models.CharField(max_length=70,default='wtxqqq')      #B选项
    ChoiceC=models.CharField(max_length=70,default='wtxqqq')     #C选项
    ChoiceD=models.CharField(max_length=70,default='wtxqqq')     #D选项
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
