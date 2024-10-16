from django.contrib import admin
from .models import Invoice, Product


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'customer_name', 'amount', 'paid_status', 'date')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'stock')


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Product, ProductAdmin)
