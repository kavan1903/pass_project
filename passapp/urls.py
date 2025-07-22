from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_invoice, name='create_invoice'),
    path('invoice/<uuid:uuid>/', views.view_invoice, name='view_invoice'),
]
