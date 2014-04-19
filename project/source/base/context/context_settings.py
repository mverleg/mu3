
import settings
print settings.__file__
from settings import BASE_TEMPLATE


'''
    put some settings into the default context 
'''
def context_settings(request):
    return {
        'BASE_TEMPLATE': BASE_TEMPLATE,
    }


