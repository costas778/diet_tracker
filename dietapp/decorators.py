from django.http import HttpResponseForbidden

def user_is_authenticated(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return wrap
