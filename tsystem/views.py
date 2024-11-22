from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .utils import *
from .decorators import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
@staff_required
def home_view(request):

    tickets = Ticket.objects.all()
    
    context = {
        'tickets': tickets,
    }

    return render(request, 'index.html', context)

@login_required(login_url='/login')
@staff_required
def get_tickets(request):
    tickets = Ticket.objects.exclude(status='Закрыт').order_by('-date_create')\
        .select_related('author')  # Используем select_related для извлечения данных о пользователе в одном запросе

    paginator = Paginator(tickets, 10)  # 10 тикетов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ticket_list = []
    for ticket in page_obj:
        ticket_data = {
            'pk': ticket.pk,
            'status': ticket.status,
            'description': ticket.description,
            'date_create': ticket.date_create,
            'author': {
                'id': ticket.author.id,
                'first_name': ticket.author.first_name,
                'last_name': ticket.author.last_name
            },
            'executor': {
                'id': ticket.executor.id if ticket.executor else None,
                'first_name': ticket.executor.first_name if ticket.executor else None,
                'last_name': ticket.executor.last_name if ticket.executor else None
            }
        }
        ticket_list.append(ticket_data)

    return JsonResponse({'tickets': ticket_list, 'has_next': page_obj.has_next(), 'has_previous': page_obj.has_previous()})


class LoginUser(DataMixin, LoginView):
    form_class = AuthForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('/login')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))
    

