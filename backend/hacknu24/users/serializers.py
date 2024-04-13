from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model

from .utils import is_valid_phone_number, is_valid_sms_code

User = get_user_model()

class UserAuthSerializer(serializers.Serializer):

    phone_number = serializers.CharField()
    name = serializers.CharField(read_only = True)
    class Meta:
        fields = ('phone_number', 'name')
        read_only_fields = ('name', )

    def validate(self, data):
        phone_number = data['phone_number']

        # Validate phone number (replace with your logic)
        if not is_valid_phone_number(phone_number):
            raise serializers.ValidationError("Invalid phone number")

        return data
    
    
class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('id', 'name', 'phone_number', 'is_active', 'is_staff')

    def validate(self, data):
        print(data)
        phone_number = data['phone_number']

        # Validate phone number (replace with your logic)
        if not is_valid_phone_number(phone_number):
            raise serializers.ValidationError("Формат номера телефона неправильный")

        return data
    

class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'phone_number')

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15, required=True)
    sms_code = serializers.CharField(max_length=6, required=True)
    access_token = serializers.CharField(max_length = 200, read_only=True)
    refresh_token = serializers.CharField(max_length = 200, read_only=True)

    def validate(self, data):
        phone_number = data['phone_number']
        sms_code = data['sms_code']

        # Validate phone number (replace with your logic)
        if not is_valid_phone_number(phone_number):
            raise serializers.ValidationError("Invalid phone number")

        # Retrieve user based on phone number
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")

        # Check if user is verified (code within expiration time)
        
        is_valid_code, status = is_valid_sms_code(phone_number, sms_code)
        
        if not is_valid_code:
            raise serializers.ValidationError(status)

        # Further authentication could go here (if needed)

        refresh = RefreshToken.for_user(user)
        data['access_token'] = str(refresh.access_token)
        data['refresh_token'] = str(refresh)  # Serialized refresh token

        return data

