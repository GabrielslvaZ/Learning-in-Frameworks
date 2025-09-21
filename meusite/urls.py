from django.urls import path
from . import views

urlpatterns = [
    path('', views.pessoas_index, name='index'),
    path('login/', views.login_view, name='login'),
    path('pessoas/', views.pessoas_list, name='pessoas_list'),
]

