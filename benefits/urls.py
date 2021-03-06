from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from benefits import views # every views that I put on the views.py

app_name = "benefits"


urlpatterns = [
    path('benefits/', views.IndexBenefits.as_view(), name="benefits_list"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)