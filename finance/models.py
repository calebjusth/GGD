from django.db import models

# Create your models here.

class Partner(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=200, blank=False, null=False, default='')
    amount = models.CharField(max_length=200, blank=False, null=False, default='')
    plegde = models.CharField(max_length=200, blank=False, null=False, default='')
    address = models.TextField()

    def __str__(self):
        return self.email
    
class DonationMethod(models.Model):
    payment_gateway_name = models.CharField(max_length=200, default='')
    image = models.ImageField(default=False, null=False)
    description = models.TextField()
    gateway_link = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.payment_gateway_name