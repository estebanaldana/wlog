from django.conf.urls import url
from app.index.views import index

urlpatterns = [
	url(r'^$', index, name='index'),
]