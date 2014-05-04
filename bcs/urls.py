from django.conf.urls import url,patterns,include
from bcs import views

urlpatterns = patterns('',
	url(r'^index/',views.index),
	url(r'^logout1/',views.logout1),
)