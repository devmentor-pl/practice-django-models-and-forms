from django.shortcuts import render
from .forms import ContactForm


def contact_view(request):

    form = ContactForm()
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            success = True

            return render(request, 'cms/contact.html', {
                'form': ContactForm(),
                'success': success
            })

    return render(request, 'cms/contact.html', {
        'form': form,
        'success': success
    })
