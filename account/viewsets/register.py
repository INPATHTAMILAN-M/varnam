from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from account.serializers.register import RegisterSerializer
from account.models.customuser import CustomUser
from drf_spectacular.utils import extend_schema

class RegisterViewSet(viewsets.ModelViewSet):
    """
    User Registration API
    Provides endpoints for user registration
    """
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    http_method_names = ['post']

    @extend_schema(
        request=RegisterSerializer,
        responses={
            201: RegisterSerializer,
            400: {'type': 'object', 'properties': {'error': {'type': 'string'}}}
        },
        description="Register a new user account",
        tags=['Authentication']
    )
    def create(self, request, *args, **kwargs):
        """
        Create a new user account
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
