from django.urls import path, include

from Storage.open_views.views import *

urlpatterns = [
    path('', main_page),
    path('verbal_riddles/', include('Storage.open_urls.vr_urls')),
]
