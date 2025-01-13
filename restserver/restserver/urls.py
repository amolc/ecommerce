from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def trigger_error(request):
    1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path("<int:org_id>/api/stores/", include('stores.urls')),
    path("<int:org_id>/api/staff/", include('staff.urls')),
    path("<int:org_id>/api/customers/", include('customers.urls')),
    path("<int:org_id>/api/categories/", include('categories.urls')),
    path("<int:org_id>/api/products/", include('products.urls')),
    path("<int:org_id>/api/orders/", include('orders.urls')),
    path('<int:org_id>/api/inventory/', include('inventory.urls')),

    path('sentry-debug/', trigger_error),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
