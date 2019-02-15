from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from app.content.views import createContent, Details, updateContent, youContents, updateYouContent, youDetailContent, deleteComment, deleteContent

urlpatterns = [
	url(r'^create/content$', login_required(createContent.as_view()), name='createContent'),
	url(r'^details$', login_required(Details), name="detail"),
	url(r'^edit/public/(?P<pk>\d+)/$', login_required(updateContent.as_view()), name="editPublic"),
	url(r'^contents$', login_required(youContents), name="youContents"),
	url(r'^edit/content/(?P<pk>\d+)/$', login_required(updateYouContent.as_view()), name="updateYouContent"),
	url(r'^contents/details$', login_required(youDetailContent), name="youDetailContent"),
	url(r'^contents/details$', login_required(deleteComment), name="deleteComment"),
	url(r'^delete/content$', login_required(deleteContent), name="deleteContent"),
]