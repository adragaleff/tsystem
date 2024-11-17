from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

def staff_required(view_func):
    def _wrapper_view(request, *args, **kwargs):
        if not request.user.groups.filter(name='supports').exists():
            return render(request, 'restricted_access.html')
        return view_func(request, *args, **kwargs)
    return _wrapper_view