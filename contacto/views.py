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
                form.save()               
            
            return redirect ('www.emol.com')
               

    else:
        form = ContactoForm

    context = {
        'form': form,
    }
    return render(request, template, context)


