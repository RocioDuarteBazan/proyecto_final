from typing import Any, Dict, Set
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models.query import QuerySet
from django.views.generic import CreateView, TemplateView, ListView, DeleteView
from .forms import RegistroForm, Usuario
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.posts.models import Post,Comment
 


class Login(LoginView):
    template_name = "usuarios/login.html"

    def get_success_url(self) -> str:
        messages.success(self.request, 'Inicio de sesión exitoso!')
        return super().get_success_url()

class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('apps.usuario:login')
    template_name = 'usuarios/registro.html'

    def get_success_url(self) -> str:
        messages.success(self.request, 'Registro exitoso!')
        print(super().get_success_url())
        return super().get_success_url()

class Logout(LogoutView):

    def get_success_url(self):
        messages.success(self.request, 'Cierre de sesión exitoso!')
        return reverse_lazy('index')
       

    

class ConfirmLogout(TemplateView):
    template_name = 'usuarios/confirm_logout.html'

class UsuariolistView(LoginRequiredMixin, ListView):
    model = Usuario
    context_object_name = 'usuarios'

    def get_queryset(self):
        queriset = super().get_queryset()
        print(queriset)
        queriset = queriset.exclude(is_superuser=True)
        return queriset
    
class UsuarioDeleteview(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'usuario/eliminar_usuario.html'
    success_url = reverse_lazy('apps.usuario:usuario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        colaborador_group = Group.objects.get(name='colaborador')
        es_colaborador = colaborador_group in self.object.groups.all()
        context['es_colaborador'] = es_colaborador
        return context

def post(self, request, *args, **kwargs):
    eliminar_comentarios = request.POST.get('eliminar_comentarios', False)
    eliminar_posts = request.POST.get('eliminar_posts', False)
    self.object = self.get_object()
    if eliminar_comentarios:
       Comment.objects.filter(usuario=self.object).delete()
    
    if eliminar_posts:
        Post.objects.filter(autor=self.object).delete()
    messages.success(request, f'Usuario {self.objact.username} eliminado correctamente')
    return self.delete(request, *args, **kwargs)


