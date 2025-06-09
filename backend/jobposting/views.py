from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import JobPosting
from .serializers import JobPostingSerializer

@api_view(['GET'])
def get_jobposting(request):
    jobposting = JobPosting.objects.all()
    serializer = JobPostingSerializer(jobposting, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_jobposting(request):
    serializer = JobPostingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
