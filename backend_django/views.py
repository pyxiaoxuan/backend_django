from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import json
import sys,os
import SqlModule 
import GetPaper
# Create your views here.
def home(request):
    return render(
        request,
        'index.html'
    )
def manifest(request):
    return render(request,'manifest.json')
def asset_manifest(request):
    return render(request,'asset-manifest.json')
def getChoicePost(request):  
    if(request.method=='POST'):
        '''
        Json=json.loads(request.body.decode())       
        Title=Json['title']
        BodyA=Json['bodyA']
        BodyB=Json['bodyB']
        BodyC=Json['bodyC']
        BodyD=Json['bodyD']
        Value=Json['value']
        '''
        Title=request.POST.get('title')
        BodyA=request.POST.get('bodyA')
        BodyB=request.POST.get('bodyB')
        BodyC=request.POST.get('bodyC')
        BodyD=request.POST.get('bodyD')
        Value=request.POST.get('value')
        Unit=request.POST.get('Unit')
        #print(Title)
        SqlModule.addSql(_QID=0,_Body=Title,_Type=0,_Unit=Unit,_TimeStamp=0,_Answer=Value,_ChoiceA=BodyA,_ChoiceB=BodyB,_ChoiceC=BodyC,_ChoiceD=BodyD)
    return HttpResponse('114514')

def getCompletionPost(request):
    if(request.method=='POST'):
        Title=request.POST.get('title')
        Answer=request.POST.get('answer')
        Unit=request.POST.get('Unit')
        SqlModule.addSql(_QID=0,_Body=Title,_Type=1,_Unit=Unit,_TimeStamp=0,_Answer=Answer,_ChoiceA='',_ChoiceB='',_ChoiceC='',_ChoiceD='')
    return HttpResponse('114514')

def getCalculationPost(request):
    if(request.method=='POST'):
        Title=request.POST.get('title')
        Answer=request.POST.get('answer')
        Unit=request.POST.get('Unit')
        QID=request.POST.get('qid')
        SqlModule.addSql(_QID=QID,_Body=Title,_Type=2,_Unit=Unit,_TimeStamp=0,_Answer=Value,_ChoiceA='',_ChoiceB='',_ChoiceC='',_ChoiceD='')
    return HttpResponse('114514')

def getEssayPost(request):
    if(request.method=='POST'):
        Title=request.POST.get('title')
        Answer=request.POST.get('answer')
        Unit=request.POST.get('Unit')
        QID=request.POST.get('qid')
        SqlModule.addSql(_QID=QID,_Body=Title,_Type=3,_Unit=Unit,_TimeStamp=0,_Answer=Value,_ChoiceA='',_ChoiceB='',_ChoiceC='',_ChoiceD='')
    return HttpResponse('114514')

def getMakePost(request):
    if(request.method=='POST'):
        Repetition=request.POST.get('repetition')
        Subject=request.POST.get('subject')
        Calculation=request.POST.get('calculation')
        Essay=request.POST.get('shortanswer')
        Date=request.POST.get('date')
        #print(Date)
        if Subject!='数据结构':
            return HttpResponse('404')
        Json=GetPaper.getpaper(Repetition,Calculation,Essay)
        Json['Date']=Date
    return HttpResponse('123.docx')