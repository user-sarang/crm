from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.campaign_list, name='campaign_list'),
	url(r'^campaign/(?P<pk>\d+)/$', views.campaign_detail, name='campaign_detail'),
	url(r'^delete-file/(?P<pk>\d+)/$', views.delete_file, name='delete_file'),
]