from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def extencion_image(value):

	if "." in value:
		image = value.split('.')[1]
		extencions = ["jpg", "png", "jpeg"]

		if image not in extencions:
			raise ValidationError(_("La imagen no tiene el formato correcto"), params={'value':value},)

		else:
			raise ValidationError(_("tu imagen no contine ninguna extencion"), params={'value':value},)

		return value
		