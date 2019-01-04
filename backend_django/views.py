from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import json
import sys,os
import SqlModule 
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
        Json=json.loads(request.body.decode().replace("'", "\""))        
        Title=Json['title']
        BodyA=Json['bodyA']
        BodyB=Json['bodyB']
        BodyC=Json['bodyC']
        BodyD=Json['bodyD']
        Value=Json['value']
        #print(Title)
        SqlModule.addSql(_QID=0,_Body=Title,_Type=0,_Unit=0,_TimeStamp=0,_Answer=Value,_ChoiceA=BodyA,_ChoiceB=BodyB,_ChoiceC=BodyC,_ChoiceD=BodyD)
    return HttpResponse('114514')

def getCompletionPost(request):
    if(request.method=='POST'):
        SqlModule.addSql(_QID=0,_Body=Title,_Type=1,_Unit=0,_TimeStamp=0,_Answer=Value,_ChoiceA='',_ChoiceB='',_ChoiceC='',_ChoiceD='')
    return HttpResponse('114514')

def getCalculationPost(request):
    if(request.method=='POST'):
        SqlModule.addSql(_QID=0,_Body=Title,_Type=1,_Unit=0,_TimeStamp=0,_Answer=Value,_ChoiceA='',_ChoiceB='',_ChoiceC='',_ChoiceD='')
    return HttpResponse('114514')

def getEssayPost(request):
    if(request.method=='POST'):
        SqlModule.addSql(_QID=0,_Body=Title,_Type=1,_Unit=0,_TimeStamp=0,_Answer=Value,_ChoiceA='',_ChoiceB='',_ChoiceC='',_ChoiceD='')
    return HttpResponse('114514')