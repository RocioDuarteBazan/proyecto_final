from typing import Set
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView 
from .forms import RegistroForm
from django.urls import reverse_lazy
from django.contrib import messages


class Login(LoginView):
    template_name = "usuarios/login.html"

    def get_success_url(self) -> str:
        messages.success(self.request, 'Inicio de sesión exitoso!')
        return super().get_success_url()

class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'usuarios/registro.html'

    def get_success_url(self) -> str:
        messages.success(self.request, 'Registro exitoso!')
        return super().get_success_url()

class Logout(LogoutView):
    success_url = reverse_lazy("index")

    def get_success_url(self):
        messages.success(self.request, 'Cierre de sesión exitoso!')
        
        success_url = self.success_url
        next_page = self.request.GET.get("next", "")
        if next_page:
            success_url = next_page
        return success_url
        
       

    

class ConfirmLogout(TemplateView):
    template_name = 'usuarios/confirm_logout.html'
    
    def get_context_data(self):
        return {"next": self.request.GET.get("next", "")}
    
