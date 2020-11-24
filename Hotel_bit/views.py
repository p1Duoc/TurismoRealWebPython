from django.shortcuts import redirect, render
from django.contrib.auth import logout as do_logout
from django.shortcuts import render, redirect
from newsletters.forms import NewsletterForm
from newsletters.views import Newsletter

# Create your views here.

def home(request):
    template = "index.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})


def habitaciones(request):
    template = "room.html"

    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
    
    else:
        form = NewsletterForm

    context = {
    'form': form,
    }
    return render (request, template, context)


def galeria(request):
    template = "galeria.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})


def sobre_nosotros(request):
    template = "about.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})


def Departamento_pucon(request):
    template = "single-room.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})

def Departamento_laserena(request):
    template = "single-room_1.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})

def Departamento_viñadelmar(request):
    template = "single-room_2.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})

def Departamento_puertovaras(request):
    template = "single-room_3.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})

def Departamento_iquique(request):
    template = "single-room_4.html"
    Newsletter(request)
    return render (request, template, {'form': NewsletterForm,})



def registro(request):
    template = "base.html"

    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
    
    else:
        form = NewsletterForm

    context = {
    'form': form,
    }
    return render (request, template, context)

    def logout(request):
        do_logout(request)
        return redirect('/')
