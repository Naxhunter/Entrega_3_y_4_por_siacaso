from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')
def base(request):
    return render(request, 'base.html')
def sol_ayu(request):
    return render(request, 'sol_ayu.html')
def mot_rec(request):
    return render(request, 'mot_rec.html')
<<<<<<< HEAD
def ayuda(request):
    return render(request, 'ayuda.html')
=======
def login(request):
    return render(request, 'login.html')
>>>>>>> 718cdc46002d5a948bc8c2c71231f1f021b97f4e

# Create your views here.
