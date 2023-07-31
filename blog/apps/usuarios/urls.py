from django.urls import path
from .views import *


urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("registro/", Registro.as_view(), name="registro"),
    path("confirm_logout/", ConfirmLogout.as_view(), name="confirm_logout"),

]
