from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice
from .forms import InvoiceForm

def home(request):
    return render(request, 'home.html')  # Create a template named 'home.html'

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()

            # ✅ Render email content from invoice.html template
            subject = '🎟️ Your Raas Fiesta Pass Invoice'
            to_email = invoice.email
            context = {'invoice': invoice}
            message = render_to_string('invoice.html', context)

            # ✅ Send the email
            email = EmailMessage(subject, message, to=[to_email])
            email.content_subtype = 'html'
            email.send()

            return redirect('view_invoice', uuid=invoice.uuid)
    else:
        form = InvoiceForm()
    return render(request, 'create_invoice.html', {'form': form})


def view_invoice(request, uuid):
    invoice = get_object_or_404(Invoice, uuid=uuid)
    return render(request, 'invoice.html', {'invoice': invoice})
