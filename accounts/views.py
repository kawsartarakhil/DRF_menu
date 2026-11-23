from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from rest_framework import status
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from .serailizers import *


class Register_View(APIView):
    permission_classes = [AllowAny]

    @extend_schema(request=RegisterSerializer,responses={201:UserSerializer})
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(UserSerializer(user).data,status=status.HTTP_201_CREATED)


class Login_View(APIView):
    permission_classes = [AllowAny]

    @extend_schema(request=LoginSerializer,responses={200:dict})
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'],password=serializer.validated_data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({"refresh":str(refresh),"access":str(refresh.access_token)})
        return Response({"message":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)


class Logout_View(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(request=LogoutSerializer,responses={200:dict})
    def post(self,request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            token = RefreshToken(serializer.validated_data['refresh'])
            token.blacklist()
            return Response({"message":"Logged out successfully"})
        except TokenError:
            return Response({"message":"Invalid token"},status=status.HTTP_400_BAD_REQUEST)


class Profile_View(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(responses={200:UserSerializer})
    def get(self,request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)