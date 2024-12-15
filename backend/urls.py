from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from backend import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    path("", include("accounts_app.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
