from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpRequest
from django.conf.urls.static import static


def trigger_error(request: HttpRequest):
    1 / 0


urlpatterns = [
    path("<int:org_id>/api/stores/", include('stores.urls')),
    path("<int:org_id>/api/staff/", include('staff.urls')),
    path("<int:org_id>/api/customers/", include('customers.urls')),
    path("<int:org_id>/api/products/", include('products.urls')),
    path("<int:org_id>/api/orders/", include('orders.urls')),
    path('<int:org_id>/api/inventory/', include('inventory.urls')),
    path('<int:org_id>/api/category/', include('category.urls')),

    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
