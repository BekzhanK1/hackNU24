from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Bank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class BankCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    cardNumber = models.CharField(max_length=16)
    expirationDate = models.DateField()

    def __str__(self) -> str:
        return self.bank.name + " - " + self.cardNumber


class CashbackCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class CashbackOffer(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    category = models.ForeignKey(CashbackCategory, on_delete=models.CASCADE)
    cashback = models.FloatField()

    def __str__(self) -> str:
        return self.category.name + " " + self.bank.name
