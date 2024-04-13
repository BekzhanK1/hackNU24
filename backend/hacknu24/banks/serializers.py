from rest_framework import serializers
from .models import BankCard

class BankCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCard
        fields = '__all__'
