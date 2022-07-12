from django.shortcuts import render

# Create your views here.
# load first html page
def loadindex(request):
    return render(request,'index.html',{'key':'value'})

def loadhome(request):
    return render(request,'home.html')