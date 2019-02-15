from django.conf.urls import url

from app.user.views import registerUser

urlpatterns = [
	url(r'^register$', registerUser.as_view(), name="register")
]