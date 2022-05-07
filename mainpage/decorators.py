from tokenize import group
from django.shortcuts import redirect
from django.http import HttpResponse

def unauthorized_user(view_func):
    def wrapper_func(request,*args,**kwarges):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return view_func(request,*args,**kwarges)
    
    return wrapper_func


def allowed_users(allowed_rolles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_rolles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('you are not allowed')
        return wrapper_func
    return decorator
