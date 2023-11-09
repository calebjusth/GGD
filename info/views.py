from django.shortcuts import redirect, render
from .forms import *
from .models import *
# Create your views here.


def home(request):
    about = About.objects.all()
    church_program = ChurchProgram.objects.all()
    charity = Charity.objects.all()
    context = {
        'about': about,
        'church_program': church_program,
        'charity': charity,
    }
    return render(request, 'info/home.html', context)

def member(request):
    if request.POST:
        form = memberform(request.POST)
        if form.is_valid():
            form.save()
        return redirect(thankyoupage)
    context = {
        'form': memberform,

    }
    return render(request, 'info/membersform.html', context)

def thankyoupage(request):

    return render(request, 'info/thankyoupage.html')