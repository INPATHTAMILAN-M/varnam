from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from account.serializers.auth import LoginSerializer
from drf_spectacular.utils import extend_schema

class LoginView(APIView):
    """
    User Login API
    """
    @extend_schema(
        request=LoginSerializer,
        responses={
            200: {'type': 'object', 'properties': {'refresh': {'type': 'string'}, 'access': {'type': 'string'}}},
            400: {'type': 'object', 'properties': {'error': {'type': 'string'}}}
        },
        description="Login with email and password to get JWT tokens",
        tags=['Authentication']
    )
    def post(self, request):
        """
        Login endpoint that returns refresh and access tokens
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
