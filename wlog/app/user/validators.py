from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validateEmail(value):
	if "@" in value:
		domain = value.split('@')[1]
		domains = ["hotmail.com", "gmail.com", "outlook.com"]

		if domain not in domains:
			raise ValidationError(_("el Email no es valido"), params={'value':value},)
	else:
		raise ValidationError(_("falta el @"), params={'value':value},)

	return value


def validatePassword(value):
	password = value
	specialChar = "[~\!@·\$%\^&\*\(\)_\+{}\":;'\[\]]"

	if not any(char.isupper() for char in password):
		raise ValidationError(_('La Contraseña debe tener al menos una mayuscula'), params={'value':value},)
	if not any(char.isdigit() for char in password):
		raise ValidationError(_('La Contraseña debe tener al menos un numero'), params={'value':value},)
	if password.count(" ") > 0:
		raise ValidationError(_('La contraseña no debe tener espacios en blanco'), params={'value':value},)
	if not any(char in specialChar for char in password):
		raise ValidationError(_('La contraseña debe tener al menos un caracter especial'), params={'value':value},)
	return value