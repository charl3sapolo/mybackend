from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDet
        exclude = ["user"]
        
class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiptentry
        exclude = ["total_amount", "total_tax"]