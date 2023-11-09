from django.urls import path
from . import views


urlpatterns =[
    path('partner/', views.partner, name="partner"),
    path('forms/', views.formpage, name='form'),
]