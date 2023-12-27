from django.urls import path
from .views import ResumeInformationView, ResumeRetrieveAPIView, ResumeRetriveView

app_name = "resume"
urlpatterns = [
    path("create/", ResumeInformationView.as_view(), name="resume-information"),
    path("view/<uuid:pk>/", ResumeRetriveView.as_view(), name="resume-view"),
    path("<uuid:pk>/", ResumeRetrieveAPIView.as_view(), name="resume-view-api"),
    
    # path("create/information/", resumeInformationView, name="information-create"),
]
