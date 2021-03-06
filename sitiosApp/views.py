from django.shortcuts import render
from .models import *
def inicio(request):
    return render(request, 'index.html')
def base(request):
    return render(request, 'base.html')
def sol_ayu(request):
    return render(request, 'sol_ayu.html')
def mot_rec(request):
    return render(request, 'mot_rec.html')
def ayuda(request):
    if(request.POST):
        correo = request.POST.get("txtEmail")
        telefono = request.POST.get("txtTel")
        descripcion = request.POST.get("txtDesc")
        imagen = request.FILES.get("txtFile")
        solicitud = solicitudayuda(
            correo= correo,
            telefono= telefono,
            descripcion= descripcion,
            imagen=imagen
        )
        contexto={"mensaje":"Solictud recibida"}
        solicitud.save()
        return render(request,"ayuda.html", contexto)
    return render(request, 'ayuda.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    if(request.POST):
        nombre = request.POST.get('txtNombre')
        email = request.POST.get('txtEmail')
        passw = request.POST.get('txtPasslog')
        usuario = CategoriaUnormal(
            nombre= nombre,
            email= email,
            contrasena= passw
        )
        contexto ={"mensaje":"Registrado con exito"}
        usuario.save()
        return render(request, 'register.html', contexto)
    return render(request, 'register.html')

def anterior(request):
    return render(request, 'trabanterior.html')
def frabajo(request):
    return render(request, 'ficha_trabajo.html')
def cuenta(request):
    return render(request, 'cuenta.html')

def register_work(request):
    if(request.POST):
        rut = request.POST.get('txtRut')
        nombre = request.POST.get('txtNombre')
        email = request.POST.get('txtEmail')
        passw = request.POST.get('txtPasslog')
        esp = request.POST.get('txtEsp')
        tel = request.POST.get('txtTel')
        usuario = CategoriaUtrabajador(
            rut = rut,
            nombre = nombre,
            email= email,
            contrasena= passw,
            especialidad=esp,
            telefono=tel
        )
        contexto ={"mensaje":"Registrado con exito"}
        usuario.save()
        return render(request, 'register_work.html', contexto)
    return render(request, 'register_work.html')
def sol_tra(request):
    return render(request, 'sol_tra.html')
def mot_rec_tr(request):
    return render(request, 'mot_rec_tr.html')
def sol_ser(request):
    if(request.POST):
        correo = request.POST.get("txtEmail")
        telefono = request.POST.get("txtTel")
        descripcion = request.POST.get("txtDesc")
        imagen = request.FILES.get("txtFile")
        solicitud = solicitudtrabajo(
            correo= correo,
            telefono= telefono,
            descripcion= descripcion,
            imagen=imagen
        )
        contexto={"mensaje":"Solictud recibida"}
        solicitud.save()
        return render(request,"sol_ser.html", contexto)
    return render(request, 'sol_ser.html')
def admini(request):
    return render(request, 'admin.html')
# Create your views here.
