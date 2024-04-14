from django.contrib import admin
from .models import Bank, BankCard, CashbackCategory, CashbackOffer

# Register your models here.

admin.site.register(Bank)
admin.site.register(BankCard)
admin.site.register(CashbackOffer)
admin.site.register(CashbackCategory)
