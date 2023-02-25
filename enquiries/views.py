from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import EnquiryForm
from .models import Enquiry


def enquiry(request):
    email = settings.DEFAULT_FROM_EMAIL

    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()
            send_mail(
                f"{enquiry.subject}",
                f"Name:{enquiry.full_name}\n\n{enquiry.description}\n\nCreated on:{enquiry.created_on}",

                enquiry.email,
                [email],
                fail_silently=False,
            )
            return redirect('enquiry_success')
    else:
        form = EnquiryForm()

    return render(request, 'enquiries/enquiry.html', {'form': form})


def enquiry_success(request):
    return render(request, 'enquiries/enquiry_success.html')