from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('alterpass/', auth_views.PasswordChangeView.as_view(template_name='alterpass.html'), name='alterpass'),
    path('alterpass/feito/', auth_views.PasswordChangeDoneView.as_view(template_name='senha_alterada.html'), name='senha_alterada'),
    path('recover/', auth_views.PasswordResetView.as_view(template_name='recover.html'), name='recover'),
    path('recover/enviado/', auth_views.PasswordResetDoneView.as_view(template_name='recover_enviado.html'), name='recover_enviado'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_confirm.html'), name='reset_confirm'),
    path('reset/feito/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_feito.html'), name='reset_feito'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('404/', views.erro_404, name='erro_404'),
    path('500/', views.erro_500, name='erro_500'),
    path('403/', views.erro_403, name='erro_403'),
]
