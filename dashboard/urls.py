from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from dashboard import views # every views that I put on the views.py

app_name = "dashboard"


urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/change_employee/', views.ChangeEmployeeJSONView.as_view(), 
    name="change_employee"),
    path('dashboard/generate_hour_employee/', views.GenerateHourJSONView.as_view(), 
    name="generate_hour_employee"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)