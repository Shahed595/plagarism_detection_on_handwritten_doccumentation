from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def store_paper(request):
    return render(request, 'store_paper.html')