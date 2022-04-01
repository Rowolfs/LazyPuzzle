from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Users.open_urls.urls')),
    path('storage/', include('Storage.open_urls.urls')),
]
