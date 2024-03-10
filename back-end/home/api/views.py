from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import jwt

# from rest_framework.decorators import api_view

def test_api(request):
    token = request.META.get('HTTP_AUTHORIZATION', None).split()[1]

    # print(request.user, request.META.get('HTTP_AUTHORIZATION'))
    # print('===>', request.user, bool(request.user))

    user = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")

    print(user)

    return JsonResponse({'message':'hello world'})

class Api(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        print(request.user.username, request.user.email)
        return  Response({'Message':'Hello world'})