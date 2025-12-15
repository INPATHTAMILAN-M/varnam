from rest_framework import serializers
from account.models.customuser import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration
    """
    password = serializers.CharField(write_only=True, help_text="User password")

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'name', 'password', 'role')
        read_only_fields = ('id', 'role')
        extra_kwargs = {
            'email': {'help_text': 'User email address'},
            'username': {'help_text': 'Username for login'},
            'name': {'help_text': 'Full name of user'},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data.get('name', '')
        )
        return user
