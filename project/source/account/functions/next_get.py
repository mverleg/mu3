
from settings import LOGIN_REDIRECT_URL
from django.utils.http import is_safe_url


'''
    decorator to extract and validate the next page in the url, 
    and pass it as an argument, otherwise falling back to login url
'''
def next_GET(func, default = LOGIN_REDIRECT_URL):
    def func_with_next(request, *args, **kwargs):
        next = default
        if 'next' in request.GET:
            if is_safe_url(url = request.GET['next'], host = request.get_host()):
                next = request.GET['next']
        return func(request, *args, next = next, **kwargs)
    return func_with_next


