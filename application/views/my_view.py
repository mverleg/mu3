
from django.shortcuts import render


def my_view(request):
	"""

		:param request:
		:return:
	"""
	return render(request, 'my_template.html', {

	})


