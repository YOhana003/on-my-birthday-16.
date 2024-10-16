from django.urls import path
from . import views

urlpatterns =[
    path('', views.invoice_list),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/<str:invoice_number>/', views.invoice_detail, name='invoice_detail'),
] 
