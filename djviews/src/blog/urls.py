from django.conf.urls import url
from django.contrib import admin


from .views import (
        post_model_list_view, 
        post_model_detail_view,
        post_model_create_view,
        post_model_update_view,
        post_model_delete_view
    )

app_name = 'blog'

urlpatterns = [
    url(r'^list/$', post_model_list_view, name='list'),
    url(r'^(?P<id>\d+)/$', post_model_detail_view, name='detail'),
    url(r'^create/$', post_model_create_view, name='create'),
    url(r'^update/(?P<id>\d+)/$', post_model_update_view, name='update'),
    url(r'delete/(?P<id>\d+)/$', post_model_delete_view, name='delete')
]
