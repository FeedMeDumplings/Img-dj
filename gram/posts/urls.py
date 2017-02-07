from django.conf.urls import url
from . import views
from .views import PostList, post_create

urlpatterns = [
		url(r'^$', PostList.as_view(), name='post_list'),
		url(r'^detail/(?P<uuid>[\w-]+)/$', views.post_detail, name='post_detail'),
		url(r'^new/$', views.post_create, name='post_create'),
]