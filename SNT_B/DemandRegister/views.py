from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import authentication, permissions

from django.contrib.auth.models import User
from .serializer import DRFSerial,CompSerial
from .models import DemandForm


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    def get(self,request):
        return Response("use post method with username and password") 
    
    
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def demandRegister(request):
    if request.method == "POST":
        serializer = DRFSerial(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("DemandForm saved successfully", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("Method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def getDR(request):
    if request.method=='GET':
        rd = DemandForm.objects.all()
        serial = DRFSerial(rd,many=True)
        return Response(serial.data)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def raiseComplaint(request):
    if request.method=='POST':
        serial = CompSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response("Success")
        else:
            return Response(serial.errors)

@api_view(['POST'])
def getRaisedDemand(request):
    if request.method == "POST":
        demand = DemandForm.objects.filter()
        return Response("Called")