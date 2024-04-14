from rest_framework import serializers
from .models import BankCard, CashbackOffer

class BankCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCard
        fields = '__all__'


class CashbackOfferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CashbackOffer
        fields = '__all__'