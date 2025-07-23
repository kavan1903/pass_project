from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # ✅ use views.home instead of just home
    path('create/', views.create_invoice, name='create_invoice'),
    path('invoice/<uuid:uuid>/', views.view_invoice, name='view_invoice'),
    path('thank-you/<uuid:uuid>/', views.thank_you, name='thank_you'),
]
