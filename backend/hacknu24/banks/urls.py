from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BankCardViewSet

router = DefaultRouter()
router.register(r'bankcards', BankCardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
