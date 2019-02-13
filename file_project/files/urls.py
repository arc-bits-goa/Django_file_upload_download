from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

from . import views


app_name = 'files_home'
urlpatterns = [
    path('', views.files_home_view, name="files_home"),
    path('download/', views.download_view, name="download_file"),
]
