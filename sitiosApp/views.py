from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')
def base(request):
    return render(request, 'base.html')

# Create your views here.
