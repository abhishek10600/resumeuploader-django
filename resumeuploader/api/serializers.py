from rest_framework import serializers

from api.models import CandidateProfile

class CandidateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = ["id", "name", "email", "dob", "state", "gender", "location", "pimage", "rdoc"]