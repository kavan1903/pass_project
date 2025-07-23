from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice
from .forms import InvoiceForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')  # Create a template named 'home.html'


from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Invoice
from .forms import InvoiceForm

@login_required
def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            remaining_amount = invoice.amount - invoice.paid_amount

            subject = '🎟️ Your Raas Fiesta Pass Invoice'
            context = {'invoice': invoice, 'remaining_amount': remaining_amount}
            message = render_to_string('invoice.html', context)

            email = EmailMessage(subject, message, to=[invoice.email])
            email.content_subtype = 'html'
            email.send()

            # Redirect to Thank You page with UUID
            return redirect('thank_you', uuid=invoice.uuid)
    else:
        form = InvoiceForm()
    return render(request, 'create_invoice.html', {'form': form})


@login_required
def thank_you(request, uuid):
    invoice = Invoice.objects.get(uuid=uuid)
    return render(request, 'thank_you.html', {'invoice': invoice})

@login_required
def view_invoice(request, uuid):
    invoice = get_object_or_404(Invoice, uuid=uuid)
    remaining_amount = invoice.amount - invoice.paid_amount
    return render(request, 'invoice.html', {
        'invoice': invoice,
        'remaining_amount': remaining_amount
    })
