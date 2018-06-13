from django.conf.urls import url
from . import views

app_name = 'chat'

urlpatterns = [
    url('ajax_dateparse/', views.ajax_dateparse, name='ajax_dateparse'),
    url('', views.post_list, name='post_list'),
]
