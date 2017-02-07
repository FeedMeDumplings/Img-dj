from django.conf.urls import url
from . import views
from .forms import SubForm

urlpatterns = [
		url(r'^$', views.sub_new, name='sub_new'),
]