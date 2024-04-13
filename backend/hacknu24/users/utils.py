from phonenumbers import geocoder, is_valid_number, NumberParseException, parse
from django.contrib.auth import get_user_model
from .models import UserSMS

from django.utils.timezone import now
from rest_framework import serializers

User = get_user_model()

def is_valid_phone_number(phone_number, country_code = "KG"):
    """
    Checks if the given phone number is valid using the phonenumbers library.

    Args:
        phone_number (str): The phone number to validate.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """

    try:
        phone_number = parse(phone_number, region=country_code)
        # Optionally check for specific country or region if needed
        if geocoder.region_code_for_number(phone_number) == 'KG':  # Check for Kazakhstan (replace as needed)
            return True
        else:
            return False
    except:
        return False
    
# Modify is_valid_sms_code to check against stored code and expiration time
def is_valid_sms_code(phone_number, sms_code):
        
    if not UserSMS.objects.filter(user__phone_number = phone_number, code = sms_code).exists():
        return (False, "User not verified. Please check your SMS code.")

    try:
        user_sms = UserSMS.objects.get(user__phone_number = phone_number, code = sms_code)
        user = User.objects.get(phone_number = phone_number)

        if user_sms.code == sms_code and user_sms.expiry_at > now():
            if user.is_active == False:
                user.is_active = True  # Mark user as verified if code matches and is not expired
                user.save()  # Update user object with verified status
        
            return (True, "User is verified")
        else:
            return (False, "SMS Code is expired")

        
    except:
        return (False, "User not verified. Please check your SMS code.")


def send_sms(phone_number, sms_code):

    print(f"{phone_number} - {sms_code}")