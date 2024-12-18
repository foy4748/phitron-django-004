"""
URL configuration for library_management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Reload Browser URL config | Useful during development
    # path("__reload__/", include("django_browser_reload.urls")),
    # Regular Paths
    path("admin/", admin.site.urls),
    path("auth/", include("auth_app.urls")),
    path("", include("book.urls")),
    # path("", TemplateView.as_view(template_name="home.html")),
]

# Adding Media Config URL at the end
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
