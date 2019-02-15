from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from app.user.forms import UserForm

class registerUser(CreateView):
	model = User
	form_class = UserForm
	template_name = 'user/register.html'
	success_url = reverse_lazy('login')

	def post(self, request):
		self.object = self.get_object
		form = self.form_class(request.POST or None)
		if form.is_valid():
			registerUser = form.save(commit=False)
			userExists = (User.objects.filter(username = form.cleaned_data.get('username')).count() >0)
			emailExists = (User.objects.filter(email = form.cleaned_data.get('email')).count() > 0)
			if userExists:
				messages.error(request, 'El usuario ya existe')
				return self.render_to_response(self.get_context_data(form=form))

			if emailExists:
				messages.error(request, 'Este email ya esta registrado')
				return self.render_to_response(self.get_context_data(form=form))

			else: 
				registerUser.save()
				return HttpResponseRedirect(self.get_success_url())
		return self.render_to_response(self.get_context_data(form=form))



		