from rest_framework import serializers
from apps.users.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'password2', 'user_type']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=validated_data['user_type'],
        )

        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        # Check if email and password are present
        if email and password:
            if User.objects.filter(email=email).exists():
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    raise serializers.ValidationError({'email': 'Invalid email'})

                # Check if the password is correct
                if not user.check_password(password):
                    raise serializers.ValidationError({'password': 'Invalid password'})

                self.context['user'] = user

                return attrs
            else:
                raise serializers.ValidationError('Email not found')
        else:
            raise serializers.ValidationError(
                {
                    'email': 'Email required',
                    'password': 'Password required',
                }
            )

class UserLogoutSerializer(serializers.Serializer):
    None