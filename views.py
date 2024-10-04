from django.shortcuts import render

# Create your views here.

def home(request):
    context={}
    return render(request, "djangoproject/home.html", context)
def about(request):
    context={}
    return render(request, "djangoproject/about.html", context)
