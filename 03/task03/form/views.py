from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, "form/contact.html",
                          {'success': True})
    else:
        form = ContactForm()

    return render(request, "form/contact.html",
                  {'form': form})
