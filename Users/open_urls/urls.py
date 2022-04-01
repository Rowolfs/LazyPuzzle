from django.urls import path, include

from Users.open_views.views import *

urlpatterns = [
    path('', main_page),
]
