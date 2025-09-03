import decimal
from xml.dom import ValidationErr
from django.db import models
from django.contrib.auth.models import User

VAT_STATUS = [
    ("VAT INCLUSIVE", "VAT"),
    ("VAT EXCLUSIVE", "NO VAT"),
]

class Items(models.Model):
    name_of_item = models.CharField(max_length=100)
    barcode = models.IntegerField(unique=True)
    price_per_unit = models.DecimalField(max_digits=12, decimal_places=2)
    number_of_units = models.IntegerField()
    vat_status = models.CharField(choices=VAT_STATUS, max_length=20)
    def __str__(self):
        return self.name_of_item
    
class Receiptentry(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="item")
    amount_inquired = models.IntegerField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    total_tax = models.DecimalField(max_digits=12, decimal_places=2)
    customer_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    receipt_no = models.CharField(max_length=20)
    
    def clean(self):
        if self.amount_inquired > self.item.number_of_units:
            raise ValidationErr(f"Insufficient inventory, only {self.item.number_of_units} is available")
    
    def save(self, **kwargs):
        self.clean()
        self.total_amount = self.item.price_per_unit * self.amount_inquired
        self.total_tax = self.total_amount * float(0.18)
        self.item.number_of_units -= self.amount_inquired#this will update the foreign field upon a save
        self.item.save()#and this will be called every time the updated foreign field changes
        
        return super().save(**kwargs)
    
class CompanyDet(models.Model):
    company_name = models.CharField(max_length=100)
    company_tin = models.CharField(max_length=12, unique=True)
    company_username = models.CharField(max_length=50)
    company_email = models.EmailField(max_length=100)
    company_phoneNo = models.IntegerField()
    password = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.company_name
    
    def save(self, **kwargs):
        if not self.pk:
            user = User.objects.create_user(username=self.company_username, password=self.password, email=self.company_email)
        self.user = user
        return super().save(**kwargs)
        
    
    

