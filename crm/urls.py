from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.campaign_list, name='campaign_list')
]