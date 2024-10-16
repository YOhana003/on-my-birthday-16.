from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Invoice

# List of invoices
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoice_list.html',
                   {'invoices': invoices})

# Detailed view of a specific invoice
def invoice_detail(request, invoice_number):
    invoice = get_object_or_404(Invoice, invoice_number=invoice_number)

    return render(request, 'invoice_detail.html',
                   {'invoice': invoice,})                 



  