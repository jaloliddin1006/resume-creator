from django.contrib import admin
from django.urls import path, include
# static settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resume.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
