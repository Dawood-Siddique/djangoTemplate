from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from apps.users.serializers.user_serializer import (
    LoginSerializer,
    RegisterSerializer,
)


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User Register Successfully'}, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_401_UNAUTHORIZED)

