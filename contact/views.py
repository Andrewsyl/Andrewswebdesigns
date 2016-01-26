from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from forms import ContactView


# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactView(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent. Thank you.')
            return HttpResponseRedirect('/contact')
        else:
            #form = ContactView()
            #messages.add_message(request, messages.ERROR, 'Your message not sent. Not enough data')
            return render(request, 'contact.html', {'form': form})

    else:
        form = ContactView()
        return render(request, 'contact.html', {'form': form})
