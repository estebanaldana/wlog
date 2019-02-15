from django.db import models
from django.conf import settings

class comments(models.Model):
	idUser = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	idContent = models.CharField(null=True, max_length=50)
	username = models.CharField(null=True, max_length=50)
	description = models.CharField(null=True, max_length=100)
	timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
	
	def __str(self):
		return '{}'.format(self.description)
