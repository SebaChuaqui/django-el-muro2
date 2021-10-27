from django.shortcuts import redirect
from django.contrib import messages

def login_required(function):

    def wrapper(request, *args, **kargs):
        if 'usuario' not in request.session:
            return redirect('/login')
        resp = function(request, *args,**kargs)
        return resp
    return wrapper
