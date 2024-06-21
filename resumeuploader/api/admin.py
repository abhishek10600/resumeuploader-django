from django.contrib import admin
from api.models import CandidateProfile

# Register your models here.

@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "dob", "state", "gender", "location", "pimage", "rdoc"]