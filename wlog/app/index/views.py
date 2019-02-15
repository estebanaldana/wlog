from django.shortcuts import render
from app.content.models import content_blog
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):

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



	return render(request, 'base/index.html', context)
