from django import forms
from app.comments.models import comments

class commentsForm(forms.ModelForm):

	class Meta:

		model = comments

		fields = [
			'username',
			'description',
		]

		labels = {
			'username':'Usuario',
			'description':'Descripcion',
		}

		widgets = {
			'username': forms.TextInput(attrs={'required':'True', 'autocomplete':'off', 'style': 'width:300px;', 'class':'form-control', 'placeholder':'Titulo'}),
			'description': forms.Textarea(attrs={'required':'True', 'autocomplete':'off', 'style': 'width:300px;', 'class':'form-control', 'placeholder':'Descripcion'}),
		}
