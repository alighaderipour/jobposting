from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import JobPosting
from .serializers import JobPostingSerializer

@api_view(['GET'])
def get_jobposting(request):
    all_jobs = JobPosting.objects.all()
    active_jobs = JobPosting.objects.filter(is_active=True)
    inactive_jobs = JobPosting.objects.filter(is_active=False)

    all_serializer = JobPostingSerializer(all_jobs, many=True)
    active_serializer = JobPostingSerializer(active_jobs, many=True)
    inactive_serializer = JobPostingSerializer(inactive_jobs, many=True)

    return Response({
        "all": all_serializer.data,
        "active": active_serializer.data,
        "inactive": inactive_serializer.data
    })

@api_view(['POST'])
def add_jobposting(request):
    serializer = JobPostingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def job_details(request, id):  # take id from URL
    job_posting_details = JobPosting.objects.get(id=id)
    jp_details_serializer = JobPostingSerializer(job_posting_details)
    return Response(jp_details_serializer.data)
