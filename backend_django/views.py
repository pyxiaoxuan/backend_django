from django.shortcuts import render

# Create your views here.
def home(request):
    return render(
        request,
        'index.html'
    )
def manifest(request):
    return render(request,'manifest.json')
def logo(request):
    return render(request,'log.png')