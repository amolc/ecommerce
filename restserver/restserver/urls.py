"""
URL configuration for restserver project.

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
from django.conf import settings
from django.conf.urls.static import static


def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path("<int:org_id>/api/customer/", include("customers.urls")),
    path("<int:org_id>/api/category/" , include('categories.urls')),
    path("<int:org_id>/api/subcategory/" , include('subcategories.urls')),
    path("<int:org_id>/api/product/" , include('product.urls')),


    path('sentry-debug/', trigger_error),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)