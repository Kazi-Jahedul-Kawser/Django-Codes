from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'navigation/about.html')

def home(request):
    return render(request,'navigation/home.html')