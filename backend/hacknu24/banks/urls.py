from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BankCardViewSet, CashbackOfferViewSet

router = DefaultRouter()
router.register(r'bankcards', BankCardViewSet)
router.register(r'cashbackoffers', CashbackOfferViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
