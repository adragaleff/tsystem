from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
# Create your views here.
def home_view(request):

    tickets = Ticket.objects.all()
    
    context = {
        'tickets': tickets,
    }

    return render(request, 'index.html', context)

def get_tickets(request):
    tickets = Ticket.objects.exclude(status='Закрыт').order_by('-date_create')\
        .select_related('author')  # Используем select_related для извлечения данных о пользователе в одном запросе

    ticket_list = []
    for ticket in tickets:
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

    return JsonResponse({'tickets': ticket_list})