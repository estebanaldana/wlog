from django.db import models
from django.conf import settings
from app.content.validators import extencion_image

class content_blog(models.Model):
	idUser = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	title = models.CharField(null=True, max_length=20)
	description = models.CharField(null=True, max_length=1000)
	image = models.FileField(null=True, upload_to='image/')
	timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
	tipeStatus = models.CharField(null=True, max_length=10)

	class Meta:
		ordering = ["-timestamp"]
