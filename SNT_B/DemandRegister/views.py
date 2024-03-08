from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DemandForm
from .serializer import DRFSerial  # Import your serializer

@api_view(['POST'])
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
def getDR(request):
    if request.method=='GET':
        rd = DemandForm.objects.all()
        serial = DRFSerial(rd,many=True)
        return Response(serial.data)