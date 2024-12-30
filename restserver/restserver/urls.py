from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def trigger_error(request):
    division_by_zero = 1 / 0  # type: ignore # noqa: F841


urlpatterns = [
    path('admin/', admin.site.urls),
    path("<int:org_id>/api/customer/", include("customers.urls")),
    path("<int:org_id>/api/category/", include('categories.urls')),
    path("<int:org_id>/api/subcategory/", include('subcategories.urls')),
    path("<int:org_id>/api/product/", include('product.urls')),
    path("<int:org_id>/api/order/", include('order.urls')),
    path("<int:org_id>/api/orderItem/", include('order_items.urls')),
    path("<int:org_id>/api/admin/", include('admins.urls')),
    path("<int:org_id>/api/staff/", include('staff.urls')),
    path("<int:org_id>/api/billing/", include('billing.urls')),
    path('<int:org_id>/api/inventory/', include('inventory.urls')),
    path("<int:org_id>/api/store/", include('store.urls')),

    path('sentry-debug/', trigger_error),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
