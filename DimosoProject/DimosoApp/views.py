from django.shortcuts import render, get_object_or_404



# Create your views here.
def base(response):
    return render(response, 'DimosoApp/base.html')
def home(response):
    
    return render(response, 'DimosoApp/home.html')
    


