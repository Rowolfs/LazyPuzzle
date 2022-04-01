from django.urls import path, include

from Storage.open_views.vr_views import *

urlpatterns = [
    path('', main_page),
    path('add/', Add_VerbalRiddles.as_view(), name="vr_add"),
    path('gallery/', Gallery_VerbalRiddles.as_view(), name="vr_gallery"),
]
