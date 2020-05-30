from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.read_user_files, name='index'),
]