from rest_framework.views import APIView
from rest_framework.response import Response
from .seralizers import RegisterSerial

class Register(APIView):
    def post(self, request):
        data = RegisterSerial(data=request.POST)
        if data.is_valid():
            data.save()
            print("user create")
        else:
            print(data.errors)
        return Response('isledi')