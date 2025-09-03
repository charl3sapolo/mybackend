from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from .models import *

class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()
    
class ItemUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()

class Receipt(generics.ListCreateAPIView):
    serializer_class = ReceiptSerializer
    queryset = Receiptentry.objects.all()
    
class CompanyEndpt(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = CompanyDet.objects.defer("password")
    
class CompanyUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = CompanyDet.objects.all()
    #this endpoint can only be accesed by an authenticated personel
