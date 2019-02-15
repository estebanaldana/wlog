import os
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage 
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from app.content.models import content_blog
from app.comments.models import comments
from app.content.forms import contentForm

class createContent(CreateView):
	model = content_blog
	template_name = 'crud/contentCreate.html'
	form_class = contentForm
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super(createContent, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST or None, request.FILES or None)
		if form.is_valid():
			content = form.save(commit=False)
			content.user = request.user
			content.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))

def Details(request):
	id_content = request.GET.get('detail') 
	instance = get_object_or_404(content_blog, id=id_content)
	instanceComments = comments.objects.filter(idContent=id_content)
	context = {
		"instance":instance,
		"instanceComments":instanceComments,
	}

	if request.method == 'POST':
		int_content = int(id_content)
		comments_text = request.POST.get('textarea')
		insert = comments(idContent=int_content, username=request.user, description= comments_text)
		insert.save()
		return render(request, 'crud/contentView.html', context)
	else:
		return render(request, 'crud/contentView.html', context)

	return render(request, 'crud/contentView.html', context)

class updateContent(UpdateView):
	model = content_blog
	template_name = 'crud/contentUpdate.html'
	form_class = contentForm
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super(updateContent, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		content = self.model.objects.get(id=pk)
		if 'form' not in context:
			context['form'] = self.form_class()
		context['id'] = pk
		return context

	def post(self,request, *args, **kwargs):
		self.object = self.get_object
		idContent = kwargs['pk']
		content =self.model.objects.get(id=idContent)
		title = request.POST.get('title')
		description = request.POST.get('description')
		form = self.form_class(request.POST, instance=content)
		if request.method == 'POST':
			self.model.objects.filter(id=idContent).update(title=title, description=description)
			return HttpResponseRedirect(self.get_success_url())
		else:
			messages.error(request, 'Upp! ocurrio un error no puedes actualiar la información')
			return HttpResponseRedirect(self.get_context_data())

def youContents(request):
	try:
		query_list = content_blog.objects.all()
		query = request.GET.get("q")
		if query:
			query_list = query_list.filter(
				Q(title__icontains=query)
				).distinct()

		paginator = Paginator(query_list, 20)
		page_request = "Pagina"
		page = request.GET.get(page_request)

		try:
		    queryset = paginator.page(page)
		except PageNotAnInteger:
			queryset = paginator.page(1)
		except EmptyPage:
			queryset = paginator.page(paginator.num_pages)

		context = {
			"object": queryset,
			"page_request": page_request
		}

	except ObjectDoesNotExist:
		query_list = None

	return render(request, 'crud/youContents.html', context)

def youDetailContent(request):
	idComment = request.GET.get('delete')
	comDelete = comments.objects.filter(id=idComment)
	comDelete.delete()
	id_content = request.GET.get('details') 
	instance = get_object_or_404(content_blog, id=id_content)
	instanceComments = comments.objects.filter(idContent=id_content)
	context = {
		"youinstance":instance,
		"youinstanceComments":instanceComments,
	}
	return render(request, 'crud/youDetailContent.html', context)

class updateYouContent(UpdateView):
	model = content_blog
	template_name = 'crud/youEditContent.html'
	form_class = contentForm
	success_url = reverse_lazy('youContents')

	def get_context_data(self, **kwargs):
		context = super(updateYouContent, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		content = self.model.objects.get(id=pk)
		if 'form' not in context:
			context['form'] = self.form_class()
		context['id'] = pk
		return context

	def post(self,request, *args, **kwargs):
		self.object = self.get_object
		idContent = kwargs['pk']
		content =self.model.objects.get(id=idContent)
		title = request.POST.get('title')
		description = request.POST.get('description')
		form = self.form_class(request.POST, instance=content)
		if request.method == 'POST':
			self.model.objects.filter(id=idContent).update(title=title, description=description)
			return HttpResponseRedirect(self.get_success_url())
		else:
			messages.error(request, 'Upp! ocurrio un error no puedes actualiar la información')
			return HttpResponseRedirect(self.get_context_data())

def deleteContent(request):
	idcontent = request.GET.get('delete')
	image = str(request.GET.get('val'))
	contDelete = content_blog.objects.filter(id=idcontent)
	comDelete = comments.objects.filter(idContent=idcontent)
	if os.path.exists(image):
		os.remove(image)
	contDelete.delete()
	comDelete.delete()
	return redirect('youContents')

def deleteComment(request):
	idReturn = request.GET.get('details')
	instance = get_object_or_404(content_blog, id=idReturn)
	instanceComments = comments.objects.filter(idContent=idReturn)
	context = {
		"youinstance":instance,
		"youinstanceComments":instanceComments,
	}
	return render(request, 'crud/youDetailContent.html', context)
