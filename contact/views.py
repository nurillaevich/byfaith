from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        print(True)
        if form.is_valid():
            form.save()
            print(False)
            return redirect('/')
    else:
        form = ContactForm()
    ctx = {
        'forms': form,
    }
    return render(request, 'contact.html', ctx)
