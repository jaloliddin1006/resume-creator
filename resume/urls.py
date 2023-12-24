from django.urls import path
from .views import ResumeInformationView

urlpatterns = [
    path("create/", ResumeInformationView.as_view(), name="resume-information"),
    # path("create/information/", resumeInformationView, name="information-create"),
]
