from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes   # ← Important: add permission_classes here

from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# ====================== Custom JWT Serializer ======================
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# ====================== Register View ======================
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response({"error": "Username and password are required"}, 
                          status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "User with this username already exists"}, 
                          status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username, 
            password=password, 
            email=email or None
        )
        return Response({
            "message": "User created successfully",
            "username": user.username
        }, status=status.HTTP_201_CREATED)


# ====================== Protected View ======================
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "You are successfully authenticated!",
            "user": request.user.username,
            "email": request.user.email,
        })


# ====================== Public Home View ======================
@api_view(['GET'])
@permission_classes([AllowAny])          # ← Now correctly imported and used
def home_view(request):
    return Response({
        "message": "Welcome to Django REST API with JWT Authentication!",
        "status": "success",
        "endpoints": {
            "Register New User": {
                "method": "POST",
                "url": "/api/register/",
                "example_body": {
                    "username": "shubhangi",
                    "password": "Pass@123",
                    "email": "shubhangi@example.com"
                }
            },
            "Login (Get Tokens)": {
                "method": "POST",
                "url": "/api/token/",
                "example_body": {
                    "username": "shubhangi",
                    "password": "Pass@123"
                }
            },
            "Refresh Token": {
                "method": "POST",
                "url": "/api/token/refresh/",
                "example_body": {"refresh": "your_refresh_token_here"}
            },
            "Protected Example": {
                "method": "GET",
                "url": "/api/protected/",
                "note": "Requires Authorization: Bearer <access_token>"
            }
        },
        "tip": "Use Thunder Client or Postman in VS Code to test easily."
    })