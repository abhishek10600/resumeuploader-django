from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.models import CandidateProfile
from api.serializers import CandidateProfileSerializer

from django.shortcuts import get_object_or_404


@api_view(["POST"])
def create_new_candidate(request):
    data = request.data
    serializer = CandidateProfileSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"candidate":serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)

@api_view(["GET"])
def get_all_candidates(request):
    candidates = CandidateProfile.objects.all()
    serializer = CandidateProfileSerializer(candidates, many=True)
    return Response({"candidates":serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_candidate(request,pk):
    candidate = get_object_or_404(CandidateProfile, id=pk)
    serializer = CandidateProfileSerializer(candidate, many=False)
    return Response({"candidate":serializer.data}, status=status.HTTP_200_OK)