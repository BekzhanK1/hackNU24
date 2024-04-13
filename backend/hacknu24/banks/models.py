from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Bank(models.Model):
    name = models.CharField(max_length=100)

class BankCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    cardNumber = models.CharField(max_length=16)
    expirationDate = models.DateField()

class CashbackCategory(models.Model):
    name = models.CharField(max_length=100)

class CashbackOffer(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    category = models.ForeignKey(CashbackCategory, on_delete=models.CASCADE)
    cashback = models.FloatField()
    condition = models.TextField()
    expirationDate = models.DateField()
    limitations = models.TextField()