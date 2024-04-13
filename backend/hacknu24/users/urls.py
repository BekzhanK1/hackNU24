from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, LoginView, UserInfoView

router = routers.DefaultRouter()
router.register(r'auth', UserViewSet, basename='auth')

urlpatterns = [
    path('users/me/', UserInfoView.as_view()),
    path('auth/verify/', LoginView.as_view()),
    path('', include(router.urls)),
]
