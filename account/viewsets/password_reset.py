from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes, smart_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings
from account.models.customuser import CustomUser
from account.serializers.password_reset import (
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer
)
from drf_spectacular.utils import extend_schema

class PasswordResetRequestView(APIView):
    """
    Password Reset Request API
    """
    @extend_schema(
        request=PasswordResetRequestSerializer,
        responses={
            200: {'type': 'object', 'properties': {'message': {'type': 'string'}}},
            400: {'type': 'object', 'properties': {'error': {'type': 'string'}}}
        },
        description="Request a password reset link",
        tags=['Authentication']
    )
    def post(self, request):
        """
        Request password reset link
        """
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = CustomUser.objects.get(email=email)
        
        # Generate token
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = PasswordResetTokenGenerator().make_token(user)
        
        # Send email with reset link
        reset_link = f"{settings.FRONTEND_URL}/reset-password/{uidb64}/{token}/"
        send_mail(
            'Password Reset Request',
            f'Click the link to reset your password: {reset_link}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        
        return Response({
            'message': 'Password reset link sent to your email.'
        }, status=status.HTTP_200_OK)

class PasswordResetConfirmView(APIView):
    """
    Password Reset Confirm API
    """
    @extend_schema(
        request=PasswordResetConfirmSerializer,
        responses={
            200: {'type': 'object', 'properties': {'message': {'type': 'string'}}},
            400: {'type': 'object', 'properties': {'error': {'type': 'string'}}}
        },
        description="Confirm password reset with token",
        tags=['Authentication']
    )
    def post(self, request):
        """
        Confirm password reset with token
        """
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        uidb64 = serializer.validated_data['uidb64']
        token = serializer.validated_data['token']
        password = serializer.validated_data['password']
        
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=user_id)
            
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({
                    'error': 'Invalid or expired token.'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            user.set_password(password)
            user.save()
            
            return Response({
                'message': 'Password reset successfully.'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': 'Failed to reset password.'
            }, status=status.HTTP_400_BAD_REQUEST)
