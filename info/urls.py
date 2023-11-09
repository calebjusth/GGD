from django.urls import path
from . import views


urlpatterns =[
    path('', views.home, name="home"),
    path('members_form/', views.member, name='member'),
    path('thanks_page/', views.thankyoupage, name='thankyoupage'),
]