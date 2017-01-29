
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index') #views.index means the function in views.py's index function
]
