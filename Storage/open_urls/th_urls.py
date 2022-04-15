from django.urls import path, include

from Storage.open_views.th_views import *

urlpatterns = [
    path('', main_page),
    path('add/', Add_Themes.as_view(), name="th_add"),
    path('gallery/', Gallery_Themes.as_view(), name="th_gallery"),
]
