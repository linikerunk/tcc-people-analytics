"""PeopleAnalytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('users.urls')),
    path('', include('performance.urls')),
    path('', include('training.urls')),
    path('', include('health.urls')),
    path('', include('ticket.urls')),
    path('', include('dashboard.urls')),
    path('', include('hour.urls')),
    path('', include('recruiting.urls')),
    path('', include('business.urls')),
    path('', include('dismissal.urls')),
    path('', include('benefits.urls')),
    path('painel/', admin.site.urls),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.AdminSite.site_header = "Enginee RH"
admin.AdminSite.site_title = "Enginee RH"
admin.AdminSite.index_title = "Enginee RH, Um sistema de gestão de funcionário."