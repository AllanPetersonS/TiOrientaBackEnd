from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import GPSData
from .serializers import GPSDataSerializer

@api_view(['POST'])
def gps_data(request):
    if request.method == 'POST':
        serializer = GPSDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)