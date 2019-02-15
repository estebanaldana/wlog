from django import forms
from app.content.models import content_blog

class contentForm(forms.ModelForm):

	class Meta:
		STATUS = (('publica','Publica'),('privada','Privada'))

		model = content_blog

		fields = [
			'title',
			'description',
			'image',
			'tipeStatus',
		]

		labels = {
			'title':'Titulo',
			'description':'Descripcion',
			'image':'Imagen',
			'tipeStatus':'Estado',
		}

		widgets = {
			'title': forms.TextInput(attrs={'required':'True', 'autocomplete':'off', 'style': 'width:300px;', 'class':'form-control', 'placeholder':'Titulo'}),
			'description': forms.Textarea(attrs={'required':'True', 'autocomplete':'off', 'style': 'width:300px;', 'class':'form-control', 'placeholder':'Descripcion'}),
			'image': forms.FileInput(attrs={'required':'True', 'class':'custom-file-input', 'accept':'image/jpeg,image/png'}),
			'tipeStatus': forms.Select(attrs={'required':'True', 'class':'custom-select'}, choices=STATUS),
		}
