from django import forms
from app.labels.models import labels

class labelsForm(forms.ModelForm):

	class Meta:

		model = labels

		fields = [
			'label',
		]

		labels = {
			'label':'Etiqueta'
		}

		widgets = {
			'label' : forms.TextInput(attr={'required':'True', 'autocomplete':'off', 'style': 'width:300px;', 'class':'form-control', 'placeholder':'Etiqueta'})
		}