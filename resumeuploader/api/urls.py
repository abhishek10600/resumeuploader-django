from django.urls import path

from api.views import create_new_candidate,get_all_candidates,get_candidate

urlpatterns = [
    path("candidates/new/",create_new_candidate, name="create_new_candidate"),
    path("candidates/all/", get_all_candidates, name="get_all_candidates"),
    path("candidates/<str:pk>/", get_candidate, name="get_candidate")
]
