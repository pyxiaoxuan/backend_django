from django.shortcuts import render,HttpResponse

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
    Title=request.POST.get('title','')
    BodyA=request.POST.get('bodyA','')
    BodyB=request.POST.get('bodyB','')
    BodyC=request.POST.get('bodyC','')
    BodyD=request.POST.get('bodyD','')
    Value=request.POST.get('value','')
    print(Title,BodyA,BodyB,BodyC,BodyD,Value)
    return HttpResponse(Title)
