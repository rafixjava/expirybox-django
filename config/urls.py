from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from items.views import home

admin.site.site_header = "ShelfLife admin"
admin.site.site_title = "ShelfLife"

urlpatterns = [
    path("", home, name="home"),
    path("accounts/", include("accounts.urls")),
    path("items/", include("items.urls")),
    path("notifications/", include("notifications.urls")),
    path("impact/", include("impact.urls")),
    path("market/", include("marketplace.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
