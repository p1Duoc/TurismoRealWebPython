from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactoForm
from newsletters.forms import NewsletterForm
# Create your views here.

def contacto(request):
    template = "contact.html"

    if request.method == "POST":
        form = ContactoForm(request.POST)

        if form.is_valid():
            form.save()

        if request.method == "POST":
            form = NewsletterForm(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, "Enviado Correctamente")
                return redirect("main:homepage")
            else:
                messages.error(request,"No enviado")
    else:
        form = ContactoForm

    context = {
        'form': form,
    }
    return render(request, template, context)


