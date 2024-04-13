from rest_framework import viewsets, status, views
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from .serializers import UserAuthSerializer, LoginSerializer, UserSerializer, AdminSerializer
from .models import User, UserSMS
from .utils import send_sms

import datetime, random

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated access to create users
    http_method_names = ['post']


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        if not User.objects.filter(phone_number = serializer.validated_data['phone_number']).exists():
            # Create the user object without saving (unverified)
            user = User.objects.create(
                phone_number=serializer.validated_data['phone_number'],
                name=serializer.validated_data.get('name', ''),
            )
            user.save()  # Save user object with verification information
        else:
            user = User.objects.get(phone_number = serializer.validated_data['phone_number'])

        # Send SMS code for verification

        generated_code = generate_sms_code(user)
        send_sms(user.phone_number, generated_code)  # Replace with your code generation logic

        # Store code (e.g., in a database) and expiration time for further verification


        sms_verification = UserSMS.objects.create(
            user = user,
            code = generated_code
        ).save()


        # user.verification_code = generate_sms_code(user)  # Replace with actual code generation
        # user.verification_code_expiry = datetime.datetime.now() + datetime.timedelta(minutes=10)  # Set an expiration time

        return Response(serializer.data, status=status.HTTP_201_CREATED)

def generate_sms_code(user):
    # Replace with your logic for generating a unique SMS code
    # return "123456"  # Placeholder code for demonstration
    return random.randint(100000, 999999)


class LoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UserInfoView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user
        print(user)
        serializer = UserSerializer(user)


        return Response({
            "user": serializer.data
        }, status=status.HTTP_200_OK)

