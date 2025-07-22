from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice
from .forms import InvoiceForm

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            return redirect('view_invoice', uuid=invoice.uuid)
    else:
        form = InvoiceForm()
    return render(request, 'create_invoice.html', {'form': form})

def view_invoice(request, uuid):
    invoice = get_object_or_404(Invoice, uuid=uuid)
    return render(request, 'invoice.html', {'invoice': invoice})
