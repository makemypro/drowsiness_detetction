from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authtoken.serializers import AuthTokenSerializer

from django.contrib.auth import login


from .distance_api import DistanceMatrixAPI

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication

from .drowsiness_detection_ml.drowsiness_detetction.drowsiness_detection import Read_Frame
from .serializers import UserSerializer, RegisterSerializer, DistanceMatrixSerializer


from django.contrib.auth.models import User


class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = request.user

        serializer = UserSerializer(user)

        return Response(serializer.data)


# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class DriverAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print("Request----------------->")
        if request.query_params.get('is_detect'):
            Read_Frame()
        return Response(status=200)


class DistanceMatrixAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = DistanceMatrixSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        origin = serializer.validated_data.get('origin')
        destination = serializer.validated_data.get('destination')
        api = DistanceMatrixAPI()
        result = api.get_distance_matrix(origin, destination)
        if result:
            return Response(data={'result': result}, status=200)

        return Response(status=400)

