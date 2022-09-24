from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.authentication import authenticate
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import  TokenAuthentication

# Create your views here.

class HomePage(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def get(self, request):
        user = request.user

        return JsonResponse({"message": f"You logged in as {user}"})


@api_view(["POST"])
@permission_classes((AllowAny,))
def login_view(request):
    if request.method == 'POST':

        password = request.data.get('password')
        username = request.data.get('username')

        user = authenticate(username=username, password=password)
        

        if(user is not None):
            if user.is_active:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return JsonResponse({"messsage": "login success", "token": str(token), "STATUS":200})

        else:
            return JsonResponse({"message": "invalid user!", "STATUS":401})
    else:
        return JsonResponse({"message": "GET request not allowed!", "STATUS":405})

@api_view(["POST"])
@permission_classes((AllowAny,))
def register_view(request):
    if(request.method == 'POST'):
        password = request.data.get('password')
        username = request.data.get('username')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        gender = request.data.get('gender')
        nationality = request.data.get('nationality')
        country = request.data.get('country')
        User.objects.create_user(password=password, username=username, email=email, first_name=first_name, last_name=last_name, gender=gender, nationality=nationality, country=country)
        return JsonResponse({"message": "User created sucessfuuly"})

    return JsonResponse({"message": "GET request not allowed!"})

