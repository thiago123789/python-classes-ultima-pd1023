from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contato/', views.contato, name='contato'),
    path('examples/', views.example_view, name='example_view')
]