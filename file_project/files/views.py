from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.conf import settings

from .models import File

import os

file_content_types = [
	'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
	'application/pdf',
	'image/png',
	'text/plain',
]

# Create your views here.
def files_home_view(request):
	context = {}

	if request.method == 'POST':
		uploaded_file = request.FILES['my_file']
		if uploaded_file.content_type not in file_content_types:
			print("INVALID CONTENT TYPE")

		else:
			new_file = File(upload=uploaded_file, file_type=uploaded_file.content_type)
			new_file.save()
			print(uploaded_file.content_type)

	qs = File.objects.all().order_by('-upload_datetime')
	context['files'] = qs

	context["file_types"] = file_content_types
	file_type_counts = []
	for file_type in file_content_types:
		count = File.objects.filter(file_type=file_type).count()
		file_type_counts.append(count)

	context["file_type_counts"] = file_type_counts

	return render(request, "files/files_home.html", context)


def download_view(request):
	if request.method == 'POST':
		path = request.POST.get('path')
		print(path)
		file_path = os.path.join(settings.MEDIA_ROOT, path)
		if os.path.exists(file_path):
			with open(file_path, 'rb') as fh:
				response = HttpResponse(fh.read(), content_type="application/force-download")
				response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
				return response
	raise Http404
    # return HttpResponse("<h1>test</h1>")