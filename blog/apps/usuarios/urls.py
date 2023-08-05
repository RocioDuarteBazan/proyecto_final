from django.urls import path
from .views import *
from . import views
from django.contrib.auth import views as auth_views

app_name = 'apps.usuario'

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("registro/", Registro.as_view(), name="registro"),
    path("confirm_logout/", ConfirmLogout.as_view(), name="confirm_logout"),
    # path('registrar/', views.RegistrarUsuario.as_view(), name='registrar'),
    #path('password_reset/', MyPasswordResetView.as_view, name='password_reset'),
    #path('password_reset/done/', MyPasswordResetDoneView.as_view, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_done'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('usuarios/', UsuariolistView.as_view(), name='usuario_list'),
    path('usuario/<int:pk>/eliminar/', UsuarioDeleteview.as_view(), name='usuario_delete'),

]
