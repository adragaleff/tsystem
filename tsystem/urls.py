from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_view, name="home"),
    path('get_tickets/', views.get_tickets, name="get_tickets"),
]