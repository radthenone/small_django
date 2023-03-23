from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from apps.users.models import User
from apps.users.serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer
from rest_framework import permissions
from django.contrib.auth import authenticate, login, logout
from apps.users.permissions import AnonPermission

# Create your views here.
class UserCreateViewSet(viewsets.ModelViewSet):

    permission_classes = [AnonPermission]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        if user:
            response_data = {
                'message': f'User {user.email} created successfully.'
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

class UserLoginViewSet(viewsets.ViewSet, generics.CreateAPIView):

    permission_classes = [AnonPermission]
    serializer_class = UserLoginSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            response_data = {
                'id': user.id,
                'email': user.email,
                'user_type': user.user_type,
                'message': 'You are logged in'
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {'message': 'Wrong login data'}
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutViewSet(viewsets.ViewSet, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserLogoutSerializer

    def post(self, request):
        logout(request)
        return Response({"message": "Successfully logout."})