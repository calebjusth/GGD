from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.

def partner(request):
     
    donation_method = DonationMethod.objects.all()
    context = {
        'donation_method': donation_method,
        'form':partnerform,
    }
    return render(request, './partner/partners.html', context)



def formpage(request):
    if request.POST:
        form = partnerform(request.POST)
        if form.is_valid():
            form.save()
        return redirect(partner)
    
    context = {
        'form':partnerform,
    }
    return render(request, './partner/forms.html', context)