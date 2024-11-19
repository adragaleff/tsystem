from django.urls import path, include
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_view, name="home"),

    path('get_tickets/', views.get_tickets, name="get_tickets"),
    path('get_ticket_detail/', views.get_ticket_detail, name="get_ticket_detail"),

    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
]