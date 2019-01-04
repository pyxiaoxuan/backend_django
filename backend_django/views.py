from django.shortcuts import render,HttpResponse
import json
import sys,os
import SqlModule 
import GetPaper
import DocModule
import time
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
        print(Repetition,Calculation,Essay)
        if Subject!='数据结构':
            return HttpResponse('404')
        Json=GetPaper.getpaper(Repetition,Calculation,Essay)
        DocModule.genPaper(time.strftime('%Y-%m-%d',time.localtime(time.time()))+'paper.docx',Json,Date)
        DocModule.genAnswer(time.strftime('%Y-%m-%d',time.localtime(time.time()))+'answer.docx',Json,Date)
    return HttpResponse('114514')

def getDocGet(request):
    List=os.listdir('%s\\backend_django\\assets'%(sys.path[0]))
    Time=[]
    for each in List:
        if(each.count('paper.docx')>=1):
            Time.append(each)
    time=Time[2]
    file=open('%s\\backend_django\\assets\\%s'%(sys.path[0],time),'rb')  
    response =HttpResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="%s"'%time 
    return response

def getAnsGet(request):
    List=os.listdir('%s\\backend_django\\assets'%(sys.path[0]))
    Time=[]
    for each in List:
        if(each.count('answer.docx')>=1):
            Time.append(each)
    time=Time[2]
    file=open('%s\\backend_django\\assets\\%s'%(sys.path[0],time),'rb')  
    response =HttpResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="%s"'%time 
    return response

def getQ1Get(request):
    List=os.listdir('%s\\backend_django\\assets'%(sys.path[0]))
    Time=[]
    for each in List:
        if(each.count('paper.docx')>=1):
            Time.append(each)
    time=Time[2]
    file=open('%s\\backend_django\\assets\\%s'%(sys.path[0],time),'rb')  
    response =HttpResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="%s"'%time 
    return response

def getQ2Get(request):
    List=os.listdir('%s\\backend_django\\assets'%(sys.path[0]))
    Time=[]
    for each in List:
        if(each.count('paper.docx')>=1):
            Time.append(each)
    time=Time[1]
    file=open('%s\\backend_django\\assets\\%s'%(sys.path[0],time),'rb')  
    response =HttpResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="%s"'%time 
    return response

def getQ3Get(request):
    List=os.listdir('%s\\backend_django\\assets'%(sys.path[0]))
    Time=[]
    for each in List:
        if(each.count('paper.docx')>=1):
            Time.append(each)
    time=Time[0]
    file=open('%s\\backend_django\\assets\\%s'%(sys.path[0],time),'rb')  
    response =HttpResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="%s"'%time 
    return response

def getA1Get(request):
    List=os.listdir('%s\\backend_django\\assets'%(sys.path[0]))
    Time=[]
    for each in List:
        if(each.count('answer.docx')>=1):
            Time.append(each)
    time=Time[2]
    file=open('%s\\backend_django\\assets\\%s'%(sys.path[0],time),'rb')  
    response =HttpResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="%s"'%time  
    return response

def getA2Get(request):
    List=os.listdir('%s\\backend_django\\assets'%(sys.path[0]))
    Time=[]
    for each in List:
        if(each.count('answer.docx')>=1):
            Time.append(each)
    time=Time[1]
    file=open('%s\\backend_django\\assets\\%s'%(sys.path[0],time),'rb')  
    response =HttpResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="%s"'%time 
    return response

def getA3Get(request):
    List=os.listdir('%s\\backend_django\\assets'%(sys.path[0]))
    Time=[]
    for each in List:
        if(each.count('answer.docx')>=1):
            Time.append(each)
    time=Time[0]
    file=open('%s\\backend_django\\assets\\%s'%(sys.path[0],time),'rb')  
    response =HttpResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="%s"'%time 
    return response

def getTimePost(request):
    List=os.listdir('%s\\backend_django\\assets'%(sys.path[0]))
    Time=[]
    for each in List:
        if(each.count('paper.docx')>=1):
            Time.append(each.strip('paper.docx'))
    print(Time)
    time={'time1':Time[2],'time2':Time[1],'time3':Time[0]}
    return HttpResponse(json.dumps(time), content_type="application/json")

def getChoiceBody(request):
    
    Json=GetPaper.getBody('0')
    return HttpResponse(json.dumps(Json), content_type="application/json")

def getDelete(request):
    ID=request.POST.get('id')
    SqlModule.delSql(int(ID))
    return HttpResponse('114514')