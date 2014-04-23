
from django.shortcuts import render
from account.models import MuUser


'''
	
'''
def my_view(request):
	return render(request, 'my_template.html', {
		
	})


