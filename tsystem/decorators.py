from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def staff_required(view_func):
    def _wrapper_view(request, *args, **kwargs):
        if not request.user.groups.filter(name='support').exists():
            return HttpResponseForbidden('<h1>Доступ ограничен</h1><p>У вас нет прав для доступа к этой странице.</p>')
        return view_func(request, *args, **kwargs)
    return _wrapper_view