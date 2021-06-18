from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')
def base(request):
    return render(request, 'base.html')
def sol_ayu(request):
    return render(request, 'sol_ayu.html')
def mot_rec(request):
    return render(request, 'mot_rec.html')
def ayuda(request):
    return render(request, 'ayuda.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')

# Create your views here.
