from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "DK Shop Admin"
admin.site.site_title = "DK MobileShop Admin Panel"
admin.site.index_title = "Welcome to DK MobileShop Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyShop.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
