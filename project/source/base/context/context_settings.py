
from settings import BASE_TEMPLATE, BASE_EMAIL_TEMPLATE


'''
    put some settings into the default context 
'''
def context_settings(request):
    return {
        'BASE_TEMPLATE': BASE_TEMPLATE,
        'BASE_EMAIL_TEMPLATE': BASE_EMAIL_TEMPLATE,
    }


